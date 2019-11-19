
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
    def deep_link_return_url(self) -> str:
        return self.get('return_url')

    @deep_link_return_url.setter
    def deep_link_return_url(self, value: str):
        self['return_url'] = value


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
        return self.get('accept_multiple')

    @accept_multiple.setter
    def accept_multiple(self, value: bool):
        self['accept_multiple'] = value


    @property
    def auto_create(self) -> bool:
        return self.get('auto_create')

    @auto_create.setter
    def auto_create(self, value: bool):
        self['auto_create'] = value


    @property
    def title(self) -> str:
        return self.get('title')

    @title.setter
    def title(self, value: str):
        self['title'] = value


    @property
    def text(self) -> str:
        return self.get('text')

    @text.setter
    def text(self, value: str):
        self['text'] = value


    @property
    def data(self) -> str:
        return self.get('data')

    @data.setter
    def data(self, value: str):
        self['data'] = value



class LTIMessage(dict):

    @property
    def iss(self) -> str:
        return self.get('iss')

    @iss.setter
    def iss(self, value: str):
        self['iss'] = value


    @property
    def sub(self) -> str:
        return self.get('sub')

    @sub.setter
    def sub(self, value: str):
        self['sub'] = value


    @property
    def given_name(self) -> str:
        return self.get('given_name')

    @given_name.setter
    def given_name(self, value: str):
        self['given_name'] = value


    @property
    def deployment_id(self) -> str:
        return self.get('https://purl.imsglobal.org/spec/lti/claim/deployment_id')

    @deployment_id.setter
    def deployment_id(self, value: str):
        self['https://purl.imsglobal.org/spec/lti/claim/deployment_id'] = value


    @property
    def message_type(self) -> str:
        return self.get('https://purl.imsglobal.org/spec/lti/claim/message_type')

    @message_type.setter
    def message_type(self, value: str):
        self['https://purl.imsglobal.org/spec/lti/claim/message_type'] = value


    @property
    def version(self) -> str:
        return self.get('https://purl.imsglobal.org/spec/lti/claim/version')

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
        return self.get('https://purl.imsglobal.org/spec/lti/claim/context')

    @context.setter
    def context(self, value: Context):
        self['https://purl.imsglobal.org/spec/lti/claim/context'] = value


    @property
    def resource_link(self) -> ResourceLink:
        return self.get('https://purl.imsglobal.org/spec/lti/claim/resource_link')

    @resource_link.setter
    def resource_link(self, value: ResourceLink):
        self['https://purl.imsglobal.org/spec/lti/claim/resource_link'] = value


    @property
    def tool_platform(self) -> ToolPlatform:
        return self.get('https://purl.imsglobal.org/spec/lti/claim/tool_platform')

    @tool_platform.setter
    def tool_platform(self, value: ToolPlatform):
        self['https://purl.imsglobal.org/spec/lti/claim/tool_platform'] = value


    @property
    def launch_presentation(self) -> LaunchPresentation:
        return self.get('https://purl.imsglobal.org/spec/lti/claim/launch_presentation')

    @launch_presentation.setter
    def launch_presentation(self, value: LaunchPresentation):
        self['https://purl.imsglobal.org/spec/lti/claim/launch_presentation'] = value


    @property
    def custom(self) -> Custom:
        return self.get('https://purl.imsglobal.org/spec/lti/claim/custom')

    @custom.setter
    def custom(self, value: Custom):
        self['https://purl.imsglobal.org/spec/lti/claim/custom'] = value


    @property
    def deep_linking_settings(self) -> DeepLinkSettings:
        return self.get('https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings')

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
        return self.get('label')

    @label.setter
    def label(self, value: str):
        self['label'] = value


    @property
    def scoreMaximum(self) -> float:
        return self.get('scoreMaximum')

    @scoreMaximum.setter
    def scoreMaximum(self, value: float):
        self['scoreMaximum'] = value


    @property
    def tag(self) -> str:
        return self.get('tag')

    @tag.setter
    def tag(self, value: str):
        self['tag'] = value


    @property
    def resourceId(self) -> str:
        return self.get('resourceId')

    @resourceId.setter
    def resourceId(self, value: str):
        self['resourceId'] = value


    @property
    def resourceLinkId(self) -> str:
        return self.get('resourceLinkId')

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
        return self.get('type')

    @type.setter
    def type(self, value: str):
        self['type'] = value


    @property
    def title(self) -> str:
        return self.get('title')

    @title.setter
    def title(self, value: str):
        self['title'] = value


    @property
    def text(self) -> str:
        return self.get('text')

    @text.setter
    def text(self, value: str):
        self['text'] = value


    @property
    def url(self) -> str:
        return self.get('url')

    @url.setter
    def url(self, value: str):
        self['url'] = value


    @property
    def custom(self) -> Dict[str,str]:
        if not 'custom' in self:
            self['custom'] = []
        return self.get('custom')

    @custom.setter
    def custom(self, value: Dict[str,str]):
        self['custom'] = value


    @property
    def line_item(self) -> LineItem:
        return self.get('lineItem')

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



