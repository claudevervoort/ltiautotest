
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
        if issubclass(bool, Enum):
            return bool(val)
        if (isinstance(val, dict) and not isinstance(val, bool)):
            typed_val = bool( **val )
            self['accept_multiple'] = typed_val
            return typed_val
        return val
            

    @accept_multiple.setter
    def accept_multiple(self, value: bool):
        if isinstance(value, Enum):
            self['accept_multiple'] = value.value
        else:
            self['accept_multiple'] = value


    @property
    def auto_create(self) -> bool:
        val = self.get('auto_create')
        if issubclass(bool, Enum):
            return bool(val)
        if (isinstance(val, dict) and not isinstance(val, bool)):
            typed_val = bool( **val )
            self['auto_create'] = typed_val
            return typed_val
        return val
            

    @auto_create.setter
    def auto_create(self, value: bool):
        if isinstance(value, Enum):
            self['auto_create'] = value.value
        else:
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



class DeeplinkResponse(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        if not self.get('https://purl.imsglobal.org/spec/lti/claim/version'):
            self['https://purl.imsglobal.org/spec/lti/claim/version'] = '1.3.0'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        if not self.get('https://purl.imsglobal.org/spec/lti/claim/message_type'):
            self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = 'LTIDeepLinkingResponse'


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



