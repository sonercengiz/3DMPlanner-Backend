from sqlmodel import Session, select
from app.infrastructure.database.models.permission_model import PermissionModel


def seed_permissions(session: Session):
    if session.exec(select(PermissionModel)).first():
        print("Permissions already exist. Skipping seed.")
        return

    # Kullanıcı
    user_mgmt = PermissionModel(name="USER_MANAGEMENT")
    user_read = PermissionModel(name="USER_READ", parent=user_mgmt)
    user_create = PermissionModel(name="USER_CREATE", parent=user_mgmt)
    user_update = PermissionModel(name="USER_UPDATE", parent=user_mgmt)
    user_delete = PermissionModel(name="USER_DELETE", parent=user_mgmt)

    # Proje
    project_mgmt = PermissionModel(name="PROJECT_MANAGEMENT")
    project_read = PermissionModel(name="PROJECT_READ", parent=project_mgmt)
    project_create = PermissionModel(name="PROJECT_CREATE", parent=project_mgmt)
    project_update = PermissionModel(name="PROJECT_UPDATE", parent=project_mgmt)
    project_delete = PermissionModel(name="PROJECT_DELETE", parent=project_mgmt)

    # Component
    component_mgmt = PermissionModel(name="COMPONENT_MANAGEMENT")
    component_read = PermissionModel(name="COMPONENT_READ", parent=component_mgmt)
    component_create = PermissionModel(name="COMPONENT_CREATE", parent=component_mgmt)
    component_update = PermissionModel(name="COMPONENT_UPDATE", parent=component_mgmt)
    component_delete = PermissionModel(name="COMPONENT_DELETE", parent=component_mgmt)

    permissions = [
        user_mgmt, user_read, user_create, user_update, user_delete,
        project_mgmt, project_read, project_create, project_update, project_delete,
        component_mgmt, component_read, component_create, component_update, component_delete
    ]

    session.add_all(permissions)
    session.commit()
    print("✅ Permissions seeded successfully.")
