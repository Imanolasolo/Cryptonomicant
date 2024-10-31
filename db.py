import sqlite3

def init_db():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    
    # Crear tabla de usuarios si no existe
    c.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        email TEXT,  -- Nueva columna para email (opcional)
        whatsapp TEXT,  -- Nueva columna para número de WhatsApp (opcional)
        first_login INTEGER DEFAULT 1  -- Nueva columna para manejar el registro inicial
    )
    ''')

    # Agregar usuario admin si no existe
    try:
        c.execute('INSERT INTO usuarios (username, password, role, first_login) VALUES (?, ?, ?, ?)', 
                  ('admin', 'admin123', 'admin', 0))  # El admin no necesita registro inicial
    except sqlite3.IntegrityError:
        pass  # Ignorar si el admin ya existe
    finally:
        conn.commit()
        conn.close()

# Función para agregar un nuevo usuario
def add_user(username, password, role, email=None, whatsapp=None):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO usuarios (username, password, role, email, whatsapp) 
            VALUES (?, ?, ?, ?, ?)
        ''', (username, password, role, email, whatsapp))
        conn.commit()
    except sqlite3.IntegrityError:
        return False  # Indica que el nombre de usuario ya existe
    finally:
        conn.close()
    return True

# Función para verificar si es la primera vez que el usuario inicia sesión
def check_first_login(username):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('SELECT first_login FROM usuarios WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

# Función para actualizar el estado de 'first_login' después del primer registro
def update_first_login(username):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('UPDATE usuarios SET first_login = 0 WHERE username = ?', (username,))
    conn.commit()
    conn.close()
