from sqlmodel import Session, select
from app.infrastructure.database.models.role_model import RoleModel
from app.infrastructure.database.models.permission_model import PermissionModel


def seed_roles(session: Session):
    if session.exec(select(RoleModel)).first():
        print("Roles already seeded.")
        return

    # Tüm yetkileri al
    permissions = session.exec(select(PermissionModel)).all()
    perms_by_name = {p.name: p for p in permissions}

    # Admin: tüm yetkilere sahip
    admin = RoleModel(
        name="ADMIN",
        permissions=permissions  # hepsi
    )

    # Editor: sadece proje ve component yazma yetkileri
    editor = RoleModel(
        name="EDITOR",
        permissions=[
            perms_by_name["PROJECT_READ"],
            perms_by_name["PROJECT_UPDATE"],
            perms_by_name["COMPONENT_READ"],
        ]
    )

    # Viewer: sadece okuma yetkisi
    viewer = RoleModel(
        name="VIEWER",
        permissions=[
            perms_by_name["PROJECT_READ"],
        ]
    )

    session.add_all([admin, editor, viewer])
    session.commit()
    print("✅ Roles seeded successfully.")
