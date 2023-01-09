from rest_framework import permissions
from rest_framework.view import Request, View
from .models import CampaignsProjects
import ipdb

class isCampaignProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: CampaignsProjects):
        ipdb.set_trace()
        return request.user == obj.owner