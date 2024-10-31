import streamlit as st
import sqlite3

# Función para conectar y obtener la base de datos
def get_db_connection():
    conn = sqlite3.connect('usuarios.db')
    return conn

# Función para obtener todos los usuarios
def get_users():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT id, username, role FROM usuarios')
    users = c.fetchall()
    conn.close()
    return users

# Función para agregar un nuevo usuario
def add_user(username, password, role, email, whatsapp):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO usuarios (username, password, role, email, whatsapp) VALUES (?, ?, ?, ?, ?)', (username, password, role, email, whatsapp))
    conn.commit()
    conn.close()

# Función para actualizar un usuario
def update_user(user_id, username, password, role, email, whatsapp):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('UPDATE usuarios SET username = ?, password = ?, role = ? WHERE id = ?', (username, password, role, user_id, role, email, whatsapp))
    conn.commit()
    conn.close()

# Función para eliminar un usuario
def delete_user(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM usuarios WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

def main():
    st.title(":red[Panel de Administración]")
    st.subheader("Gestión de Usuarios")

    # Crear un selector para el CRUD
    menu = st.selectbox("Seleccione una opción:", ["Ver Usuarios", "Agregar Usuario", "Editar Usuario", "Eliminar Usuario"])

    if menu == "Ver Usuarios":
        st.write("### Lista de Usuarios")
        users = get_users()
        if users:
            for user in users:
                user_id, username, role = user
                st.write(f"**ID:** {user_id} | **Usuario:** {username} | **Rol:** {role}")
        else:
            st.warning("No hay usuarios registrados.")
    
    elif menu == "Agregar Usuario":
        st.write("### Agregar Nuevo Usuario")
        with st.form(key='add_user_form'):
            new_username = st.text_input("Nuevo Usuario")
            new_password = st.text_input("Contraseña", type='password')
            new_role = st.selectbox("Rol", ["admin", "freemium", "premium", "pro"])
            new_email = st.text_input("Nuevo Email")
            new_whatsapp = st.text_input("Nuevo Whatsapp")
            add_user_button = st.form_submit_button("Agregar Usuario")

            if add_user_button:
                add_user(new_username, new_password, new_role, new_email, new_whatsapp)
                st.success(f"Usuario {new_username} agregado.")
                st.experimental_rerun()  # Recargar la página

    elif menu == "Editar Usuario":
        st.write("### Editar Usuario")
        users = get_users()
        if users:
            user_to_edit = st.selectbox("Seleccione el usuario a editar:", users, format_func=lambda user: f"{user[1]} ({user[2]})")
            if user_to_edit:
                edit_user_id = user_to_edit[0]
                edit_username = user_to_edit[1]
                edit_role = user_to_edit[2]

                with st.form(key='edit_user_form'):
                    edit_password = st.text_input("Nueva Contraseña", type='password')
                    edit_role_select = st.selectbox("Nuevo Rol", ["admin", "freemium", "premium", "pro"], index=["admin", "freemium", "premium", "pro"].index(edit_role))
                    update_user_button = st.form_submit_button("Actualizar Usuario")

                    if update_user_button:
                        update_user(edit_user_id, edit_username, edit_password, edit_role_select)
                        st.success(f"Usuario {edit_username} actualizado.")
                        st.experimental_rerun()  # Recargar la página
        else:
            st.warning("No hay usuarios para editar.")

    elif menu == "Eliminar Usuario":
        st.write("### Eliminar Usuario")
        users = get_users()
        if users:
            user_to_delete = st.selectbox("Seleccione el usuario a eliminar:", users, format_func=lambda user: f"{user[1]} ({user[2]})")
            if user_to_delete:
                if st.button(f"Eliminar {user_to_delete[1]}"):
                    delete_user(user_to_delete[0])
                    st.success(f"Usuario {user_to_delete[1]} eliminado.")
                    st.experimental_rerun()  # Recargar la página
        else:
            st.warning("No hay usuarios para eliminar.")

    # Opción para cambiar de usuario
    if st.button("Cambiar Usuario"):
        # Limpiar la sesión actual
        for key in list(st.session_state.keys()):
            del st.session_state[key]  # Elimina la sesión actual
        st.success("Cierre de sesión exitoso. Por favor inicie sesión de nuevo.")
        st.experimental_rerun()  # Recargar para redirigir a la página de inicio de sesión

if __name__ == "__main__":
    main()
