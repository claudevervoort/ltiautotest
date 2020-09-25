
# generated file! see gen_model.py
from typing import List, Set, Dict, Tuple, Optional
from enum import Enum
from datetime import datetime

        
class Context(dict):
    pass


class ResourceLink(dict):
    pass


class ToolPlatform(dict):
    pass


class LaunchPresentation(dict):
    pass


class Custom(dict):
    pass


class DeeplinkSettings(dict):

    @property
    def return_url(self) -> str:
        val = self.get('deep_link_return_url')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['deep_link_return_url'] = typed_val
            return typed_val
        return val


    @return_url.setter
    def return_url(self, value: str):
        if isinstance(value, Enum):
            self['deep_link_return_url'] = value.value
        else:
            self['deep_link_return_url'] = value


    @property
    def accept_types(self) -> List[str]:
        if not 'accept_types' in self:
            self['accept_types'] = []
        return self.get('accept_types')

    @accept_types.setter
    def accept_types(self, value: List[str]):
        self['accept_types'] = value


    @property
    def accept_media_types(self) -> List[str]:
        if not 'accept_media_types' in self:
            self['accept_media_types'] = []
        return self.get('accept_media_types')

    @accept_media_types.setter
    def accept_media_types(self, value: List[str]):
        self['accept_media_types'] = value


    @property
    def accept_presentation_document_targets(self) -> List[str]:
        if not 'accept_presentation_document_targets' in self:
            self['accept_presentation_document_targets'] = []
        return self.get('accept_presentation_document_targets')

    @accept_presentation_document_targets.setter
    def accept_presentation_document_targets(self, value: List[str]):
        self['accept_presentation_document_targets'] = value


    @property
    def accept_multiple(self) -> bool:
        val = self.get('accept_multiple')
        if (val):
            if type(val) is bool:
                return val
            # Moodle error encoded a string
            if type(val) is str:
                return val.lower() == 'true'
            return False
        return None

    @accept_multiple.setter
    def accept_multiple(self, value: bool):
        self['accept_multiple'] = value


    @property
    def auto_create(self) -> bool:
        val = self.get('auto_create')
        if (val):
            if type(val) is bool:
                return val
            # Moodle error encoded a string
            if type(val) is str:
                return val.lower() == 'true'
            return False
        return None

    @auto_create.setter
    def auto_create(self, value: bool):
        self['auto_create'] = value


    @property
    def title(self) -> str:
        val = self.get('title')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['title'] = typed_val
            return typed_val
        return val


    @title.setter
    def title(self, value: str):
        if isinstance(value, Enum):
            self['title'] = value.value
        else:
            self['title'] = value


    @property
    def text(self) -> str:
        val = self.get('text')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['text'] = typed_val
            return typed_val
        return val


    @text.setter
    def text(self, value: str):
        if isinstance(value, Enum):
            self['text'] = value.value
        else:
            self['text'] = value


    @property
    def data(self) -> str:
        val = self.get('data')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['data'] = typed_val
            return typed_val
        return val


    @data.setter
    def data(self, value: str):
        if isinstance(value, Enum):
            self['data'] = value.value
        else:
            self['data'] = value



class GradeService(dict):

    @property
    def lineitem(self) -> str:
        val = self.get('lineitem')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['lineitem'] = typed_val
            return typed_val
        return val


    @lineitem.setter
    def lineitem(self, value: str):
        if isinstance(value, Enum):
            self['lineitem'] = value.value
        else:
            self['lineitem'] = value


    @property
    def lineitems(self) -> str:
        val = self.get('lineitems')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['lineitems'] = typed_val
            return typed_val
        return val


    @lineitems.setter
    def lineitems(self, value: str):
        if isinstance(value, Enum):
            self['lineitems'] = value.value
        else:
            self['lineitems'] = value


    @property
    def scope(self) -> List[str]:
        if not 'scope' in self:
            self['scope'] = []
        return self.get('scope')

    @scope.setter
    def scope(self, value: List[str]):
        self['scope'] = value



class MembershipService(dict):

    @property
    def context_memberships_url(self) -> str:
        val = self.get('context_memberships_url')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['context_memberships_url'] = typed_val
            return typed_val
        return val


    @context_memberships_url.setter
    def context_memberships_url(self, value: str):
        if isinstance(value, Enum):
            self['context_memberships_url'] = value.value
        else:
            self['context_memberships_url'] = value


    @property
    def service_version(self) -> str:
        val = self.get('service_version')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['service_version'] = typed_val
            return typed_val
        return val


    @service_version.setter
    def service_version(self, value: str):
        if isinstance(value, Enum):
            self['service_version'] = value.value
        else:
            self['service_version'] = value



class LTIMessage(dict):

    @property
    def iss(self) -> str:
        val = self.get('iss')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['iss'] = typed_val
            return typed_val
        return val


    @iss.setter
    def iss(self, value: str):
        if isinstance(value, Enum):
            self['iss'] = value.value
        else:
            self['iss'] = value


    @property
    def sub(self) -> str:
        val = self.get('sub')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['sub'] = typed_val
            return typed_val
        return val


    @sub.setter
    def sub(self, value: str):
        if isinstance(value, Enum):
            self['sub'] = value.value
        else:
            self['sub'] = value


    @property
    def given_name(self) -> str:
        val = self.get('given_name')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['given_name'] = typed_val
            return typed_val
        return val


    @given_name.setter
    def given_name(self, value: str):
        if isinstance(value, Enum):
            self['given_name'] = value.value
        else:
            self['given_name'] = value


    @property
    def family_name(self) -> str:
        val = self.get('family_name')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['family_name'] = typed_val
            return typed_val
        return val


    @family_name.setter
    def family_name(self, value: str):
        if isinstance(value, Enum):
            self['family_name'] = value.value
        else:
            self['family_name'] = value


    @property
    def name(self) -> str:
        val = self.get('name')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['name'] = typed_val
            return typed_val
        return val


    @name.setter
    def name(self, value: str):
        if isinstance(value, Enum):
            self['name'] = value.value
        else:
            self['name'] = value


    @property
    def email(self) -> str:
        val = self.get('email')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['email'] = typed_val
            return typed_val
        return val


    @email.setter
    def email(self, value: str):
        if isinstance(value, Enum):
            self['email'] = value.value
        else:
            self['email'] = value


    @property
    def deployment_id(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/deployment_id')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] = typed_val
            return typed_val
        return val


    @deployment_id.setter
    def deployment_id(self, value: str):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] = value


    @property
    def target_link_uri(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/target_link_uri')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/target_link_uri'] = typed_val
            return typed_val
        return val


    @target_link_uri.setter
    def target_link_uri(self, value: str):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/target_link_uri'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/target_link_uri'] = value


    @property
    def message_type(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/message_type')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = typed_val
            return typed_val
        return val


    @message_type.setter
    def message_type(self, value: str):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = value


    @property
    def version(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/version')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/version'] = typed_val
            return typed_val
        return val


    @version.setter
    def version(self, value: str):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/version'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/version'] = value


    @property
    def role(self) -> List[str]:
        if not 'https://purl.imsglobal.org/spec/lti/claim/roles' in self:
            self['https://purl.imsglobal.org/spec/lti/claim/roles'] = []
        return self.get('https://purl.imsglobal.org/spec/lti/claim/roles')

    @role.setter
    def role(self, value: List[str]):
        self['https://purl.imsglobal.org/spec/lti/claim/roles'] = value


    @property
    def context(self) -> Context:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/context')
        if issubclass(Context, Enum):
            return Context(val)
        if (isinstance(val, dict) and not isinstance(val, Context)):
            typed_val = Context( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/context'] = typed_val
            return typed_val
        return val


    @context.setter
    def context(self, value: Context):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/context'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/context'] = value


    @property
    def resource_link(self) -> ResourceLink:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/resource_link')
        if issubclass(ResourceLink, Enum):
            return ResourceLink(val)
        if (isinstance(val, dict) and not isinstance(val, ResourceLink)):
            typed_val = ResourceLink( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/resource_link'] = typed_val
            return typed_val
        return val


    @resource_link.setter
    def resource_link(self, value: ResourceLink):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/resource_link'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/resource_link'] = value


    @property
    def tool_platform(self) -> ToolPlatform:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/tool_platform')
        if issubclass(ToolPlatform, Enum):
            return ToolPlatform(val)
        if (isinstance(val, dict) and not isinstance(val, ToolPlatform)):
            typed_val = ToolPlatform( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/tool_platform'] = typed_val
            return typed_val
        return val


    @tool_platform.setter
    def tool_platform(self, value: ToolPlatform):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/tool_platform'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/tool_platform'] = value


    @property
    def launch_presentation(self) -> LaunchPresentation:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/launch_presentation')
        if issubclass(LaunchPresentation, Enum):
            return LaunchPresentation(val)
        if (isinstance(val, dict) and not isinstance(val, LaunchPresentation)):
            typed_val = LaunchPresentation( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/launch_presentation'] = typed_val
            return typed_val
        return val


    @launch_presentation.setter
    def launch_presentation(self, value: LaunchPresentation):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/launch_presentation'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/launch_presentation'] = value


    @property
    def custom(self) -> Custom:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/custom')
        if issubclass(Custom, Enum):
            return Custom(val)
        if (isinstance(val, dict) and not isinstance(val, Custom)):
            typed_val = Custom( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/custom'] = typed_val
            return typed_val
        return val


    @custom.setter
    def custom(self, value: Custom):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/custom'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/custom'] = value


    @property
    def deep_linking_settings(self) -> DeeplinkSettings:
        val = self.get('https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings')
        if issubclass(DeeplinkSettings, Enum):
            return DeeplinkSettings(val)
        if (isinstance(val, dict) and not isinstance(val, DeeplinkSettings)):
            typed_val = DeeplinkSettings( **val )
            self['https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'] = typed_val
            return typed_val
        return val


    @deep_linking_settings.setter
    def deep_linking_settings(self, value: DeeplinkSettings):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'] = value


    @property
    def grade_service(self) -> GradeService:
        val = self.get('https://purl.imsglobal.org/spec/lti-ags/claim/endpoint')
        if issubclass(GradeService, Enum):
            return GradeService(val)
        if (isinstance(val, dict) and not isinstance(val, GradeService)):
            typed_val = GradeService( **val )
            self['https://purl.imsglobal.org/spec/lti-ags/claim/endpoint'] = typed_val
            return typed_val
        return val


    @grade_service.setter
    def grade_service(self, value: GradeService):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti-ags/claim/endpoint'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti-ags/claim/endpoint'] = value


    @property
    def membership_service(self) -> MembershipService:
        val = self.get('https://purl.imsglobal.org/spec/lti-nrps/claim/namesroleservice')
        if issubclass(MembershipService, Enum):
            return MembershipService(val)
        if (isinstance(val, dict) and not isinstance(val, MembershipService)):
            typed_val = MembershipService( **val )
            self['https://purl.imsglobal.org/spec/lti-nrps/claim/namesroleservice'] = typed_val
            return typed_val
        return val


    @membership_service.setter
    def membership_service(self, value: MembershipService):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti-nrps/claim/namesroleservice'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti-nrps/claim/namesroleservice'] = value



class DeeplinkResponse(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        if not self.get('https://purl.imsglobal.org/spec/lti/claim/version'):
            self['https://purl.imsglobal.org/spec/lti/claim/version'] = '1.3.0'


        if not self.get('https://purl.imsglobal.org/spec/lti/claim/message_type'):
            self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = 'LtiDeepLinkingResponse'


    @property
    def version(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/version')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/version'] = typed_val
            return typed_val
        return val


    @version.setter
    def version(self, value: str):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/version'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/version'] = value


    @property
    def message_type(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/message_type')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = typed_val
            return typed_val
        return val


    @message_type.setter
    def message_type(self, value: str):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = value


    @property
    def data(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti-dl/claim/data')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti-dl/claim/data'] = typed_val
            return typed_val
        return val


    @data.setter
    def data(self, value: str):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti-dl/claim/data'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti-dl/claim/data'] = value


    @property
    def deployment_id(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/deployment_id')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] = typed_val
            return typed_val
        return val


    @deployment_id.setter
    def deployment_id(self, value: str):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] = value


    @property
    def content_items(self) -> List:
        if not 'https://purl.imsglobal.org/spec/lti-dl/claim/content_items' in self:
            self['https://purl.imsglobal.org/spec/lti-dl/claim/content_items'] = []
        return self.get('https://purl.imsglobal.org/spec/lti-dl/claim/content_items')

    @content_items.setter
    def content_items(self, value: List):
        self['https://purl.imsglobal.org/spec/lti-dl/claim/content_items'] = value



class LineItem(dict):

    mime = 'application/vnd.ims.lis.v2.lineitem+json'


    mime_collection = 'application/vnd.ims.lis.v2.lineitemcontainer+json'


    read_scope = 'https://purl.imsglobal.org/spec/lti-ags/scope/lineitem.readonly'


    write_scope = 'https://purl.imsglobal.org/spec/lti-ags/scope/lineitem'


    @property
    def id(self) -> str:
        val = self.get('id')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['id'] = typed_val
            return typed_val
        return val


    @id.setter
    def id(self, value: str):
        if isinstance(value, Enum):
            self['id'] = value.value
        else:
            self['id'] = value


    @property
    def label(self) -> str:
        val = self.get('label')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['label'] = typed_val
            return typed_val
        return val


    @label.setter
    def label(self, value: str):
        if isinstance(value, Enum):
            self['label'] = value.value
        else:
            self['label'] = value


    @property
    def scoreMaximum(self) -> float:
        val = self.get('scoreMaximum')
        if issubclass(float, Enum):
            return float(val)
        if (isinstance(val, dict) and not isinstance(val, float)):
            typed_val = float( **val )
            self['scoreMaximum'] = typed_val
            return typed_val
        return val


    @scoreMaximum.setter
    def scoreMaximum(self, value: float):
        if isinstance(value, Enum):
            self['scoreMaximum'] = value.value
        else:
            self['scoreMaximum'] = value


    @property
    def tag(self) -> str:
        val = self.get('tag')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['tag'] = typed_val
            return typed_val
        return val


    @tag.setter
    def tag(self, value: str):
        if isinstance(value, Enum):
            self['tag'] = value.value
        else:
            self['tag'] = value


    @property
    def resourceId(self) -> str:
        val = self.get('resourceId')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['resourceId'] = typed_val
            return typed_val
        return val


    @resourceId.setter
    def resourceId(self, value: str):
        if isinstance(value, Enum):
            self['resourceId'] = value.value
        else:
            self['resourceId'] = value


    @property
    def resourceLinkId(self) -> str:
        val = self.get('resourceLinkId')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['resourceLinkId'] = typed_val
            return typed_val
        return val


    @resourceLinkId.setter
    def resourceLinkId(self, value: str):
        if isinstance(value, Enum):
            self['resourceLinkId'] = value.value
        else:
            self['resourceLinkId'] = value


    @property
    def startDateTime(self) -> str:
        val = self.get('startDateTime')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['startDateTime'] = typed_val
            return typed_val
        return val


    @startDateTime.setter
    def startDateTime(self, value: str):
        if isinstance(value, Enum):
            self['startDateTime'] = value.value
        else:
            self['startDateTime'] = value


    @property
    def endDateTime(self) -> str:
        val = self.get('endDateTime')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['endDateTime'] = typed_val
            return typed_val
        return val


    @endDateTime.setter
    def endDateTime(self, value: str):
        if isinstance(value, Enum):
            self['endDateTime'] = value.value
        else:
            self['endDateTime'] = value




class GradingProgress(Enum):



    NOTREADY = 'NotReady'


    FAILED = 'Failed'


    PENDING = 'Pending'


    PENDINGMANUAL = 'PendingManual'


    FULLYGRADED = 'FullyGraded'




class ActivityProgress(Enum):



    INITIALIZED = 'Initialized'


    STARTED = 'Started'


    INPROGRESS = 'InProgress'


    SUBMITTED = 'Submitted'


    COMPLETED = 'Completed'



class Score(dict):

    @property
    def userId(self) -> str:
        val = self.get('userId')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['userId'] = typed_val
            return typed_val
        return val


    @userId.setter
    def userId(self, value: str):
        if isinstance(value, Enum):
            self['userId'] = value.value
        else:
            self['userId'] = value


    @property
    def scoreGiven(self) -> float:
        val = self.get('scoreGiven')
        if issubclass(float, Enum):
            return float(val)
        if (isinstance(val, dict) and not isinstance(val, float)):
            typed_val = float( **val )
            self['scoreGiven'] = typed_val
            return typed_val
        return val


    @scoreGiven.setter
    def scoreGiven(self, value: float):
        if isinstance(value, Enum):
            self['scoreGiven'] = value.value
        else:
            self['scoreGiven'] = value


    @property
    def scoreMaximum(self) -> float:
        val = self.get('scoreMaximum')
        if issubclass(float, Enum):
            return float(val)
        if (isinstance(val, dict) and not isinstance(val, float)):
            typed_val = float( **val )
            self['scoreMaximum'] = typed_val
            return typed_val
        return val


    @scoreMaximum.setter
    def scoreMaximum(self, value: float):
        if isinstance(value, Enum):
            self['scoreMaximum'] = value.value
        else:
            self['scoreMaximum'] = value


    @property
    def comment(self) -> str:
        val = self.get('comment')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['comment'] = typed_val
            return typed_val
        return val


    @comment.setter
    def comment(self, value: str):
        if isinstance(value, Enum):
            self['comment'] = value.value
        else:
            self['comment'] = value


    @property
    def timestamp(self) -> datetime:
        val = self.get('timestamp')
        if (val):
            return datetime.fromisoformat(val)
        return None

    @timestamp.setter
    def timestamp(self, value: datetime):
        self['timestamp'] = value.isoformat()


    @property
    def activityProgress(self) -> ActivityProgress:
        val = self.get('activityProgress')
        if issubclass(ActivityProgress, Enum):
            return ActivityProgress(val)
        if (isinstance(val, dict) and not isinstance(val, ActivityProgress)):
            typed_val = ActivityProgress( **val )
            self['activityProgress'] = typed_val
            return typed_val
        return val


    @activityProgress.setter
    def activityProgress(self, value: ActivityProgress):
        if isinstance(value, Enum):
            self['activityProgress'] = value.value
        else:
            self['activityProgress'] = value


    @property
    def gradingProgress(self) -> GradingProgress:
        val = self.get('gradingProgress')
        if issubclass(GradingProgress, Enum):
            return GradingProgress(val)
        if (isinstance(val, dict) and not isinstance(val, GradingProgress)):
            typed_val = GradingProgress( **val )
            self['gradingProgress'] = typed_val
            return typed_val
        return val


    @gradingProgress.setter
    def gradingProgress(self, value: GradingProgress):
        if isinstance(value, Enum):
            self['gradingProgress'] = value.value
        else:
            self['gradingProgress'] = value



class Result(dict):

    @property
    def userId(self) -> str:
        val = self.get('userId')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['userId'] = typed_val
            return typed_val
        return val


    @userId.setter
    def userId(self, value: str):
        if isinstance(value, Enum):
            self['userId'] = value.value
        else:
            self['userId'] = value


    @property
    def resultScore(self) -> float:
        val = self.get('resultScore')
        if issubclass(float, Enum):
            return float(val)
        if (isinstance(val, dict) and not isinstance(val, float)):
            typed_val = float( **val )
            self['resultScore'] = typed_val
            return typed_val
        return val


    @resultScore.setter
    def resultScore(self, value: float):
        if isinstance(value, Enum):
            self['resultScore'] = value.value
        else:
            self['resultScore'] = value


    @property
    def resultMaximum(self) -> float:
        val = self.get('resultMaximum')
        if issubclass(float, Enum):
            return float(val)
        if (isinstance(val, dict) and not isinstance(val, float)):
            typed_val = float( **val )
            self['resultMaximum'] = typed_val
            return typed_val
        return val


    @resultMaximum.setter
    def resultMaximum(self, value: float):
        if isinstance(value, Enum):
            self['resultMaximum'] = value.value
        else:
            self['resultMaximum'] = value


    @property
    def comment(self) -> str:
        val = self.get('comment')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['comment'] = typed_val
            return typed_val
        return val


    @comment.setter
    def comment(self, value: str):
        if isinstance(value, Enum):
            self['comment'] = value.value
        else:
            self['comment'] = value


    @property
    def timestamp(self) -> str:
        val = self.get('timestamp')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['timestamp'] = typed_val
            return typed_val
        return val


    @timestamp.setter
    def timestamp(self, value: str):
        if isinstance(value, Enum):
            self['timestamp'] = value.value
        else:
            self['timestamp'] = value



class DLIFrame(dict):

    @property
    def width(self) -> float:
        val = self.get('width')
        if issubclass(float, Enum):
            return float(val)
        if (isinstance(val, dict) and not isinstance(val, float)):
            typed_val = float( **val )
            self['width'] = typed_val
            return typed_val
        return val


    @width.setter
    def width(self, value: float):
        if isinstance(value, Enum):
            self['width'] = value.value
        else:
            self['width'] = value


    @property
    def height(self) -> float:
        val = self.get('height')
        if issubclass(float, Enum):
            return float(val)
        if (isinstance(val, dict) and not isinstance(val, float)):
            typed_val = float( **val )
            self['height'] = typed_val
            return typed_val
        return val


    @height.setter
    def height(self, value: float):
        if isinstance(value, Enum):
            self['height'] = value.value
        else:
            self['height'] = value



class DLWindow(dict):

    @property
    def targetName(self) -> str:
        val = self.get('targetName')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['targetName'] = typed_val
            return typed_val
        return val


    @targetName.setter
    def targetName(self, value: str):
        if isinstance(value, Enum):
            self['targetName'] = value.value
        else:
            self['targetName'] = value



class LTIResourceLink(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        if not self.get('type'):
            self['type'] = 'ltiResourceLink'


    @property
    def type(self) -> str:
        val = self.get('type')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['type'] = typed_val
            return typed_val
        return val


    @type.setter
    def type(self, value: str):
        if isinstance(value, Enum):
            self['type'] = value.value
        else:
            self['type'] = value


    @property
    def title(self) -> str:
        val = self.get('title')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['title'] = typed_val
            return typed_val
        return val


    @title.setter
    def title(self, value: str):
        if isinstance(value, Enum):
            self['title'] = value.value
        else:
            self['title'] = value


    @property
    def text(self) -> str:
        val = self.get('text')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['text'] = typed_val
            return typed_val
        return val


    @text.setter
    def text(self, value: str):
        if isinstance(value, Enum):
            self['text'] = value.value
        else:
            self['text'] = value


    @property
    def url(self) -> str:
        val = self.get('url')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['url'] = typed_val
            return typed_val
        return val


    @url.setter
    def url(self, value: str):
        if isinstance(value, Enum):
            self['url'] = value.value
        else:
            self['url'] = value


    @property
    def custom(self) -> Dict[str,str]:
        if not 'custom' in self:
            self['custom'] = {}
        return self.get('custom')

    @custom.setter
    def custom(self, value: Dict[str,str]):
        self['custom'] = value


    @property
    def line_item(self) -> LineItem:
        val = self.get('lineItem')
        if issubclass(LineItem, Enum):
            return LineItem(val)
        if (isinstance(val, dict) and not isinstance(val, LineItem)):
            typed_val = LineItem( **val )
            self['lineItem'] = typed_val
            return typed_val
        return val


    @line_item.setter
    def line_item(self, value: LineItem):
        if isinstance(value, Enum):
            self['lineItem'] = value.value
        else:
            self['lineItem'] = value


    @property
    def max_points(self) -> float:
        if self.get('lineItem'):
            return self.get('lineItem').get('scoreMaximum')

    @max_points.setter
    def max_points(self, value: float):
        if not self.get('lineItem'):
            self['lineItem'] = LineItem()
        self['lineItem']['scoreMaximum'] = value


    @property
    def resource_id(self) -> float:
        if self.get('lineItem'):
            return self.get('lineItem').get('resourceId')

    @resource_id.setter
    def resource_id(self, value: float):
        if not self.get('lineItem'):
            self['lineItem'] = LineItem()
        self['lineItem']['resourceId'] = value


    @property
    def iframe(self) -> DLIFrame:
        val = self.get('iframe')
        if issubclass(DLIFrame, Enum):
            return DLIFrame(val)
        if (isinstance(val, dict) and not isinstance(val, DLIFrame)):
            typed_val = DLIFrame( **val )
            self['iframe'] = typed_val
            return typed_val
        return val


    @iframe.setter
    def iframe(self, value: DLIFrame):
        if isinstance(value, Enum):
            self['iframe'] = value.value
        else:
            self['iframe'] = value


    @property
    def window(self) -> DLWindow:
        val = self.get('window')
        if issubclass(DLWindow, Enum):
            return DLWindow(val)
        if (isinstance(val, dict) and not isinstance(val, DLWindow)):
            typed_val = DLWindow( **val )
            self['window'] = typed_val
            return typed_val
        return val


    @window.setter
    def window(self, value: DLWindow):
        if isinstance(value, Enum):
            self['window'] = value.value
        else:
            self['window'] = value




class MemberStatus(Enum):



    ACTIVE = 'Active'


    INACTIVE = 'Inactive'


    DELETED = 'Deleted'



class Member(dict):

    @property
    def status(self) -> MemberStatus:
        val = self.get('status')
        if issubclass(MemberStatus, Enum):
            return MemberStatus(val)
        if (isinstance(val, dict) and not isinstance(val, MemberStatus)):
            typed_val = MemberStatus( **val )
            self['status'] = typed_val
            return typed_val
        return val


    @status.setter
    def status(self, value: MemberStatus):
        if isinstance(value, Enum):
            self['status'] = value.value
        else:
            self['status'] = value


    @property
    def context_id(self) -> str:
        val = self.get('context_id')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['context_id'] = typed_val
            return typed_val
        return val


    @context_id.setter
    def context_id(self, value: str):
        if isinstance(value, Enum):
            self['context_id'] = value.value
        else:
            self['context_id'] = value


    @property
    def context_label(self) -> str:
        val = self.get('context_label')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['context_label'] = typed_val
            return typed_val
        return val


    @context_label.setter
    def context_label(self, value: str):
        if isinstance(value, Enum):
            self['context_label'] = value.value
        else:
            self['context_label'] = value


    @property
    def context_title(self) -> str:
        val = self.get('context_title')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['context_title'] = typed_val
            return typed_val
        return val


    @context_title.setter
    def context_title(self, value: str):
        if isinstance(value, Enum):
            self['context_title'] = value.value
        else:
            self['context_title'] = value


    @property
    def name(self) -> str:
        val = self.get('name')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['name'] = typed_val
            return typed_val
        return val


    @name.setter
    def name(self, value: str):
        if isinstance(value, Enum):
            self['name'] = value.value
        else:
            self['name'] = value


    @property
    def picture(self) -> str:
        val = self.get('picture')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['picture'] = typed_val
            return typed_val
        return val


    @picture.setter
    def picture(self, value: str):
        if isinstance(value, Enum):
            self['picture'] = value.value
        else:
            self['picture'] = value


    @property
    def given_name(self) -> str:
        val = self.get('given_name')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['given_name'] = typed_val
            return typed_val
        return val


    @given_name.setter
    def given_name(self, value: str):
        if isinstance(value, Enum):
            self['given_name'] = value.value
        else:
            self['given_name'] = value


    @property
    def family_name(self) -> str:
        val = self.get('family_name')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['family_name'] = typed_val
            return typed_val
        return val


    @family_name.setter
    def family_name(self, value: str):
        if isinstance(value, Enum):
            self['family_name'] = value.value
        else:
            self['family_name'] = value


    @property
    def middle_name(self) -> str:
        val = self.get('middle_name')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['middle_name'] = typed_val
            return typed_val
        return val


    @middle_name.setter
    def middle_name(self, value: str):
        if isinstance(value, Enum):
            self['middle_name'] = value.value
        else:
            self['middle_name'] = value


    @property
    def email(self) -> str:
        val = self.get('email')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['email'] = typed_val
            return typed_val
        return val


    @email.setter
    def email(self, value: str):
        if isinstance(value, Enum):
            self['email'] = value.value
        else:
            self['email'] = value


    @property
    def user_id(self) -> str:
        val = self.get('user_id')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['user_id'] = typed_val
            return typed_val
        return val


    @user_id.setter
    def user_id(self, value: str):
        if isinstance(value, Enum):
            self['user_id'] = value.value
        else:
            self['user_id'] = value


    @property
    def roles(self) -> List[str]:
        if not 'roles' in self:
            self['roles'] = []
        return self.get('roles')

    @roles.setter
    def roles(self, value: List[str]):
        self['roles'] = value



class Members(dict):

    mime = 'application/vnd.ims.lti-nrps.v2.membershipcontainer+json'


    read_scope = 'https://purl.imsglobal.org/spec/lti-nrps/scope/contextmembership.readonly'


    collection_attribute = 'members'


    @property
    def id(self) -> str:
        val = self.get('id')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['id'] = typed_val
            return typed_val
        return val


    @id.setter
    def id(self, value: str):
        if isinstance(value, Enum):
            self['id'] = value.value
        else:
            self['id'] = value


    @property
    def members(self) -> List[Member]:
        if not 'members' in self:
            self['members'] = []
        return self.get('members')

    @members.setter
    def members(self, value: List[Member]):
        self['members'] = value



class PlatformConfig(dict):

    @property
    def product_family_code(self) -> str:
        val = self.get('product_family_code')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['product_family_code'] = typed_val
            return typed_val
        return val


    @product_family_code.setter
    def product_family_code(self, value: str):
        if isinstance(value, Enum):
            self['product_family_code'] = value.value
        else:
            self['product_family_code'] = value


    @property
    def variables(self) -> List[str]:
        if not 'variables' in self:
            self['variables'] = []
        return self.get('variables')

    @variables.setter
    def variables(self, value: List[str]):
        self['variables'] = value



class PlatformOIDCConfig(dict):

    @property
    def issuer(self) -> str:
        val = self.get('issuer')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['issuer'] = typed_val
            return typed_val
        return val


    @issuer.setter
    def issuer(self, value: str):
        if isinstance(value, Enum):
            self['issuer'] = value.value
        else:
            self['issuer'] = value


    @property
    def authorization_endpoint(self) -> str:
        val = self.get('authorization_endpoint')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['authorization_endpoint'] = typed_val
            return typed_val
        return val


    @authorization_endpoint.setter
    def authorization_endpoint(self, value: str):
        if isinstance(value, Enum):
            self['authorization_endpoint'] = value.value
        else:
            self['authorization_endpoint'] = value


    @property
    def token_endpoint(self) -> str:
        val = self.get('token_endpoint')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['token_endpoint'] = typed_val
            return typed_val
        return val


    @token_endpoint.setter
    def token_endpoint(self, value: str):
        if isinstance(value, Enum):
            self['token_endpoint'] = value.value
        else:
            self['token_endpoint'] = value


    @property
    def token_endpoint_auth_methods_supported(self) -> List[str]:
        if not 'token_endpoint_auth_methods_supported' in self:
            self['token_endpoint_auth_methods_supported'] = []
        return self.get('token_endpoint_auth_methods_supported')

    @token_endpoint_auth_methods_supported.setter
    def token_endpoint_auth_methods_supported(self, value: List[str]):
        self['token_endpoint_auth_methods_supported'] = value


    @property
    def token_endpoint_auth_signing_alg_values_supported(self) -> List[str]:
        if not 'token_endpoint_auth_signing_alg_values_supported' in self:
            self['token_endpoint_auth_signing_alg_values_supported'] = []
        return self.get('token_endpoint_auth_signing_alg_values_supported')

    @token_endpoint_auth_signing_alg_values_supported.setter
    def token_endpoint_auth_signing_alg_values_supported(self, value: List[str]):
        self['token_endpoint_auth_signing_alg_values_supported'] = value


    @property
    def jwks_uri(self) -> str:
        val = self.get('jwks_uri')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['jwks_uri'] = typed_val
            return typed_val
        return val


    @jwks_uri.setter
    def jwks_uri(self, value: str):
        if isinstance(value, Enum):
            self['jwks_uri'] = value.value
        else:
            self['jwks_uri'] = value


    @property
    def registration_endpoint(self) -> str:
        val = self.get('registration_endpoint')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['registration_endpoint'] = typed_val
            return typed_val
        return val


    @registration_endpoint.setter
    def registration_endpoint(self, value: str):
        if isinstance(value, Enum):
            self['registration_endpoint'] = value.value
        else:
            self['registration_endpoint'] = value


    @property
    def scopes_supported(self) -> List[str]:
        if not 'scopes_supported' in self:
            self['scopes_supported'] = []
        return self.get('scopes_supported')

    @scopes_supported.setter
    def scopes_supported(self, value: List[str]):
        self['scopes_supported'] = value


    @property
    def response_types_supported(self) -> List[str]:
        if not 'response_types_supported' in self:
            self['response_types_supported'] = []
        return self.get('response_types_supported')

    @response_types_supported.setter
    def response_types_supported(self, value: List[str]):
        self['response_types_supported'] = value


    @property
    def subject_types_supported(self) -> List[str]:
        if not 'subject_types_supported' in self:
            self['subject_types_supported'] = []
        return self.get('subject_types_supported')

    @subject_types_supported.setter
    def subject_types_supported(self, value: List[str]):
        self['subject_types_supported'] = value


    @property
    def id_token_signing_alg_values_supported(self) -> List[str]:
        if not 'id_token_signing_alg_values_supported' in self:
            self['id_token_signing_alg_values_supported'] = []
        return self.get('id_token_signing_alg_values_supported')

    @id_token_signing_alg_values_supported.setter
    def id_token_signing_alg_values_supported(self, value: List[str]):
        self['id_token_signing_alg_values_supported'] = value


    @property
    def claims_supported(self) -> List[str]:
        if not 'claims_supported' in self:
            self['claims_supported'] = []
        return self.get('claims_supported')

    @claims_supported.setter
    def claims_supported(self, value: List[str]):
        self['claims_supported'] = value


    @property
    def lti_config(self) -> PlatformConfig:
        val = self.get('https://purl.imsglobal.org/spec/lti-platform-configuration')
        if issubclass(PlatformConfig, Enum):
            return PlatformConfig(val)
        if (isinstance(val, dict) and not isinstance(val, PlatformConfig)):
            typed_val = PlatformConfig( **val )
            self['https://purl.imsglobal.org/spec/lti-platform-configuration'] = typed_val
            return typed_val
        return val


    @lti_config.setter
    def lti_config(self, value: PlatformConfig):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti-platform-configuration'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti-platform-configuration'] = value



class MessageDef(dict):

    @property
    def type(self) -> str:
        val = self.get('type')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['type'] = typed_val
            return typed_val
        return val


    @type.setter
    def type(self, value: str):
        if isinstance(value, Enum):
            self['type'] = value.value
        else:
            self['type'] = value


    @property
    def allowLearner(self) -> bool:
        val = self.get('allowLearner')
        if (val):
            if type(val) is bool:
                return val
            # Moodle error encoded a string
            if type(val) is str:
                return val.lower() == 'true'
            return False
        return None

    @allowLearner.setter
    def allowLearner(self, value: bool):
        self['allowLearner'] = value


    @property
    def target_link_uri(self) -> str:
        val = self.get('target_link_uri')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['target_link_uri'] = typed_val
            return typed_val
        return val


    @target_link_uri.setter
    def target_link_uri(self, value: str):
        if isinstance(value, Enum):
            self['target_link_uri'] = value.value
        else:
            self['target_link_uri'] = value


    @property
    def label(self) -> str:
        val = self.get('label')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['label'] = typed_val
            return typed_val
        return val


    @label.setter
    def label(self, value: str):
        if isinstance(value, Enum):
            self['label'] = value.value
        else:
            self['label'] = value


    @property
    def placements(self) -> List[str]:
        if not 'placements' in self:
            self['placements'] = []
        return self.get('placements')

    @placements.setter
    def placements(self, value: List[str]):
        self['placements'] = value



class ToolConfig(dict):

    @property
    def domain(self) -> str:
        val = self.get('domain')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['domain'] = typed_val
            return typed_val
        return val


    @domain.setter
    def domain(self, value: str):
        if isinstance(value, Enum):
            self['domain'] = value.value
        else:
            self['domain'] = value


    @property
    def description(self) -> str:
        val = self.get('description')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['description'] = typed_val
            return typed_val
        return val


    @description.setter
    def description(self, value: str):
        if isinstance(value, Enum):
            self['description'] = value.value
        else:
            self['description'] = value


    @property
    def target_link_uri(self) -> str:
        val = self.get('target_link_uri')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['target_link_uri'] = typed_val
            return typed_val
        return val


    @target_link_uri.setter
    def target_link_uri(self, value: str):
        if isinstance(value, Enum):
            self['target_link_uri'] = value.value
        else:
            self['target_link_uri'] = value


    @property
    def custom_parameters(self) -> Custom:
        val = self.get('custom_parameters')
        if issubclass(Custom, Enum):
            return Custom(val)
        if (isinstance(val, dict) and not isinstance(val, Custom)):
            typed_val = Custom( **val )
            self['custom_parameters'] = typed_val
            return typed_val
        return val


    @custom_parameters.setter
    def custom_parameters(self, value: Custom):
        if isinstance(value, Enum):
            self['custom_parameters'] = value.value
        else:
            self['custom_parameters'] = value


    @property
    def scopes(self) -> List[str]:
        if not 'scopes' in self:
            self['scopes'] = []
        return self.get('scopes')

    @scopes.setter
    def scopes(self, value: List[str]):
        self['scopes'] = value


    @property
    def claims(self) -> List[str]:
        if not 'claims' in self:
            self['claims'] = []
        return self.get('claims')

    @claims.setter
    def claims(self, value: List[str]):
        self['claims'] = value


    @property
    def messages(self) -> List[MessageDef]:
        if not 'messages' in self:
            self['messages'] = []
        return self.get('messages')

    @messages.setter
    def messages(self, value: List[MessageDef]):
        self['messages'] = value



class ToolOIDCConfig(dict):

    @property
    def client_id(self) -> str:
        val = self.get('client_id')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['client_id'] = typed_val
            return typed_val
        return val


    @client_id.setter
    def client_id(self, value: str):
        if isinstance(value, Enum):
            self['client_id'] = value.value
        else:
            self['client_id'] = value


    @property
    def registration_client_uri(self) -> str:
        val = self.get('registration_client_uri')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['registration_client_uri'] = typed_val
            return typed_val
        return val


    @registration_client_uri.setter
    def registration_client_uri(self, value: str):
        if isinstance(value, Enum):
            self['registration_client_uri'] = value.value
        else:
            self['registration_client_uri'] = value


    @property
    def application_type(self) -> str:
        val = self.get('application_type')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['application_type'] = typed_val
            return typed_val
        return val


    @application_type.setter
    def application_type(self, value: str):
        if isinstance(value, Enum):
            self['application_type'] = value.value
        else:
            self['application_type'] = value


    @property
    def response_types(self) -> List[str]:
        if not 'response_types' in self:
            self['response_types'] = []
        return self.get('response_types')

    @response_types.setter
    def response_types(self, value: List[str]):
        self['response_types'] = value


    @property
    def grant_types(self) -> List[str]:
        if not 'grant_types' in self:
            self['grant_types'] = []
        return self.get('grant_types')

    @grant_types.setter
    def grant_types(self, value: List[str]):
        self['grant_types'] = value


    @property
    def initiate_login_uri(self) -> str:
        val = self.get('initiate_login_uri')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['initiate_login_uri'] = typed_val
            return typed_val
        return val


    @initiate_login_uri.setter
    def initiate_login_uri(self, value: str):
        if isinstance(value, Enum):
            self['initiate_login_uri'] = value.value
        else:
            self['initiate_login_uri'] = value


    @property
    def redirect_uris(self) -> List[str]:
        if not 'redirect_uris' in self:
            self['redirect_uris'] = []
        return self.get('redirect_uris')

    @redirect_uris.setter
    def redirect_uris(self, value: List[str]):
        self['redirect_uris'] = value


    @property
    def client_name(self) -> str:
        val = self.get('client_name')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['client_name'] = typed_val
            return typed_val
        return val


    @client_name.setter
    def client_name(self, value: str):
        if isinstance(value, Enum):
            self['client_name'] = value.value
        else:
            self['client_name'] = value


    @property
    def jwks_uri(self) -> str:
        val = self.get('jwks_uri')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['jwks_uri'] = typed_val
            return typed_val
        return val


    @jwks_uri.setter
    def jwks_uri(self, value: str):
        if isinstance(value, Enum):
            self['jwks_uri'] = value.value
        else:
            self['jwks_uri'] = value


    @property
    def logo_uri(self) -> str:
        val = self.get('logo_uri')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['logo_uri'] = typed_val
            return typed_val
        return val


    @logo_uri.setter
    def logo_uri(self, value: str):
        if isinstance(value, Enum):
            self['logo_uri'] = value.value
        else:
            self['logo_uri'] = value


    @property
    def token_endpoint_auth_method(self) -> str:
        val = self.get('token_endpoint_auth_method')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['token_endpoint_auth_method'] = typed_val
            return typed_val
        return val


    @token_endpoint_auth_method.setter
    def token_endpoint_auth_method(self, value: str):
        if isinstance(value, Enum):
            self['token_endpoint_auth_method'] = value.value
        else:
            self['token_endpoint_auth_method'] = value


    @property
    def contacts(self) -> List[str]:
        if not 'contacts' in self:
            self['contacts'] = []
        return self.get('contacts')

    @contacts.setter
    def contacts(self, value: List[str]):
        self['contacts'] = value


    @property
    def scope(self) -> str:
        val = self.get('scope')
        if issubclass(str, Enum):
            return str(val)
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['scope'] = typed_val
            return typed_val
        return val


    @scope.setter
    def scope(self, value: str):
        if isinstance(value, Enum):
            self['scope'] = value.value
        else:
            self['scope'] = value


    @property
    def lti_config(self) -> ToolConfig:
        val = self.get('https://purl.imsglobal.org/spec/lti-tool-configuration')
        if issubclass(ToolConfig, Enum):
            return ToolConfig(val)
        if (isinstance(val, dict) and not isinstance(val, ToolConfig)):
            typed_val = ToolConfig( **val )
            self['https://purl.imsglobal.org/spec/lti-tool-configuration'] = typed_val
            return typed_val
        return val


    @lti_config.setter
    def lti_config(self, value: ToolConfig):
        if isinstance(value, Enum):
            self['https://purl.imsglobal.org/spec/lti-tool-configuration'] = value.value
        else:
            self['https://purl.imsglobal.org/spec/lti-tool-configuration'] = value



