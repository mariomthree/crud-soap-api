from spyne import ServiceBase, rpc, Unicode, Array
from models import User, ResponseData
import controllers


class UserService(ServiceBase):

    @rpc(Unicode, Unicode, Unicode, _returns=Unicode)
    def add_user(ctx, name, email, description):
        return controllers.add_user(name, email, description)

    @rpc(Unicode, _returns=ResponseData)
    def get_user(ctx, user_id):
        user = controllers.get_user(user_id)
        if user:
            user = User(
                id=user['id'],
                name=user['name'],
                email=user['email'],
                description=user['description']
            )
            return ResponseData(user=user, success='1', message='User found')
        return ResponseData(user=User(), success='0', message='User not found.')

    @rpc(_returns=ResponseData)
    def get_users(ctx):
        users = controllers.list_users()
        if users:
            users_data = [User(
                id=user['id'],
                name=user['name'],
                email=user['email'],
                description=user['description']
            ) for user in users]
            return ResponseData(users=users_data, success='1', message="Users found.")
        return ResponseData(users=None, success='0', message="No users found.")

    @rpc(Unicode, Unicode, Unicode, Unicode, _returns=ResponseData)
    def update_user(ctx, user_id, name, email, description):
        success = controllers.update_user(user_id, name, email, description)
        message = "User updated successfully" if success else "User not found"
        return ResponseData(user=User(), success='1' if success else '0', message=message)

    @rpc(Unicode, _returns=ResponseData)
    def delete_user(ctx, user_id):
        success = controllers.delete_user(user_id)
        message = "User deleted successfully" if success else "User not found"
        return ResponseData(user=User(), success='1' if success else '0', message=message)
