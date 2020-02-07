
# generated file! see gen_model.py
from typing import List, Set, Dict, Tuple, Optional


        
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


class DeepLinkSettings(dict):

    @property
    def return_url(self) -> str:
        val = self.get('deep_link_return_url')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['deep_link_return_url'] = typed_val
            return typed_val
        return val
            

    @return_url.setter
    def return_url(self, value: str):
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
        if (isinstance(val, dict) and not isinstance(val, bool)):
            typed_val = bool( **val )
            self['accept_multiple'] = typed_val
            return typed_val
        return val
            

    @accept_multiple.setter
    def accept_multiple(self, value: bool):
        self['accept_multiple'] = value


    @property
    def auto_create(self) -> bool:
        val = self.get('auto_create')
        if (isinstance(val, dict) and not isinstance(val, bool)):
            typed_val = bool( **val )
            self['auto_create'] = typed_val
            return typed_val
        return val
            

    @auto_create.setter
    def auto_create(self, value: bool):
        self['auto_create'] = value


    @property
    def title(self) -> str:
        val = self.get('title')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['title'] = typed_val
            return typed_val
        return val
            

    @title.setter
    def title(self, value: str):
        self['title'] = value


    @property
    def text(self) -> str:
        val = self.get('text')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['text'] = typed_val
            return typed_val
        return val
            

    @text.setter
    def text(self, value: str):
        self['text'] = value


    @property
    def data(self) -> str:
        val = self.get('data')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['data'] = typed_val
            return typed_val
        return val
            

    @data.setter
    def data(self, value: str):
        self['data'] = value



class LTIMessage(dict):

    @property
    def iss(self) -> str:
        val = self.get('iss')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['iss'] = typed_val
            return typed_val
        return val
            

    @iss.setter
    def iss(self, value: str):
        self['iss'] = value


    @property
    def sub(self) -> str:
        val = self.get('sub')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['sub'] = typed_val
            return typed_val
        return val
            

    @sub.setter
    def sub(self, value: str):
        self['sub'] = value


    @property
    def given_name(self) -> str:
        val = self.get('given_name')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['given_name'] = typed_val
            return typed_val
        return val
            

    @given_name.setter
    def given_name(self, value: str):
        self['given_name'] = value


    @property
    def deployment_id(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/deployment_id')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] = typed_val
            return typed_val
        return val
            

    @deployment_id.setter
    def deployment_id(self, value: str):
        self['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] = value


    @property
    def message_type(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/message_type')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = typed_val
            return typed_val
        return val
            

    @message_type.setter
    def message_type(self, value: str):
        self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = value


    @property
    def version(self) -> str:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/version')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/version'] = typed_val
            return typed_val
        return val
            

    @version.setter
    def version(self, value: str):
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
        if (isinstance(val, dict) and not isinstance(val, Context)):
            typed_val = Context( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/context'] = typed_val
            return typed_val
        return val
            

    @context.setter
    def context(self, value: Context):
        self['https://purl.imsglobal.org/spec/lti/claim/context'] = value


    @property
    def resource_link(self) -> ResourceLink:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/resource_link')
        if (isinstance(val, dict) and not isinstance(val, ResourceLink)):
            typed_val = ResourceLink( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/resource_link'] = typed_val
            return typed_val
        return val
            

    @resource_link.setter
    def resource_link(self, value: ResourceLink):
        self['https://purl.imsglobal.org/spec/lti/claim/resource_link'] = value


    @property
    def tool_platform(self) -> ToolPlatform:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/tool_platform')
        if (isinstance(val, dict) and not isinstance(val, ToolPlatform)):
            typed_val = ToolPlatform( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/tool_platform'] = typed_val
            return typed_val
        return val
            

    @tool_platform.setter
    def tool_platform(self, value: ToolPlatform):
        self['https://purl.imsglobal.org/spec/lti/claim/tool_platform'] = value


    @property
    def launch_presentation(self) -> LaunchPresentation:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/launch_presentation')
        if (isinstance(val, dict) and not isinstance(val, LaunchPresentation)):
            typed_val = LaunchPresentation( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/launch_presentation'] = typed_val
            return typed_val
        return val
            

    @launch_presentation.setter
    def launch_presentation(self, value: LaunchPresentation):
        self['https://purl.imsglobal.org/spec/lti/claim/launch_presentation'] = value


    @property
    def custom(self) -> Custom:
        val = self.get('https://purl.imsglobal.org/spec/lti/claim/custom')
        if (isinstance(val, dict) and not isinstance(val, Custom)):
            typed_val = Custom( **val )
            self['https://purl.imsglobal.org/spec/lti/claim/custom'] = typed_val
            return typed_val
        return val
            

    @custom.setter
    def custom(self, value: Custom):
        self['https://purl.imsglobal.org/spec/lti/claim/custom'] = value


    @property
    def deep_linking_settings(self) -> DeepLinkSettings:
        val = self.get('https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings')
        if (isinstance(val, dict) and not isinstance(val, DeepLinkSettings)):
            typed_val = DeepLinkSettings( **val )
            self['https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'] = typed_val
            return typed_val
        return val
            

    @deep_linking_settings.setter
    def deep_linking_settings(self, value: DeepLinkSettings):
        self['https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings'] = value



class DeeplinkResponse(dict):

    @property
    def content_items(self) -> List:
        if not 'https://purl.imsglobal.org/spec/lti-dl/claim/content_items' in self:
            self['https://purl.imsglobal.org/spec/lti-dl/claim/content_items'] = []
        return self.get('https://purl.imsglobal.org/spec/lti-dl/claim/content_items')

    @content_items.setter
    def content_items(self, value: List):
        self['https://purl.imsglobal.org/spec/lti-dl/claim/content_items'] = value



class LineItem(dict):

    @property
    def label(self) -> str:
        val = self.get('label')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['label'] = typed_val
            return typed_val
        return val
            

    @label.setter
    def label(self, value: str):
        self['label'] = value


    @property
    def scoreMaximum(self) -> float:
        val = self.get('scoreMaximum')
        if (isinstance(val, dict) and not isinstance(val, float)):
            typed_val = float( **val )
            self['scoreMaximum'] = typed_val
            return typed_val
        return val
            

    @scoreMaximum.setter
    def scoreMaximum(self, value: float):
        self['scoreMaximum'] = value


    @property
    def tag(self) -> str:
        val = self.get('tag')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['tag'] = typed_val
            return typed_val
        return val
            

    @tag.setter
    def tag(self, value: str):
        self['tag'] = value


    @property
    def resourceId(self) -> str:
        val = self.get('resourceId')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['resourceId'] = typed_val
            return typed_val
        return val
            

    @resourceId.setter
    def resourceId(self, value: str):
        self['resourceId'] = value


    @property
    def resourceLinkId(self) -> str:
        val = self.get('resourceLinkId')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['resourceLinkId'] = typed_val
            return typed_val
        return val
            

    @resourceLinkId.setter
    def resourceLinkId(self, value: str):
        self['resourceLinkId'] = value



class LTIResourceLink(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        if not self.get('type'):
            self['type'] = 'ltiResourceLink'


    @property
    def type(self) -> str:
        val = self.get('type')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['type'] = typed_val
            return typed_val
        return val
            

    @type.setter
    def type(self, value: str):
        self['type'] = value


    @property
    def title(self) -> str:
        val = self.get('title')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['title'] = typed_val
            return typed_val
        return val
            

    @title.setter
    def title(self, value: str):
        self['title'] = value


    @property
    def text(self) -> str:
        val = self.get('text')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['text'] = typed_val
            return typed_val
        return val
            

    @text.setter
    def text(self, value: str):
        self['text'] = value


    @property
    def url(self) -> str:
        val = self.get('url')
        if (isinstance(val, dict) and not isinstance(val, str)):
            typed_val = str( **val )
            self['url'] = typed_val
            return typed_val
        return val
            

    @url.setter
    def url(self, value: str):
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
        if (isinstance(val, dict) and not isinstance(val, LineItem)):
            typed_val = LineItem( **val )
            self['lineItem'] = typed_val
            return typed_val
        return val
            

    @line_item.setter
    def line_item(self, value: LineItem):
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



