from rest_framework import permissions

# 外部キー(owner)と一致するユーザー以外は、読み取り専用とする（追加・更新・削除操作不可）
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
