class _const(object):
    
    def __setattr__(self,name,value):
        if self.__dict__.get(name):
            raise self.TypeError
        self.__dict__[name]=value

const = _const()
const.dl = _const()
const.dl.request_msg_type = 'LtiDeepLinkingRequest'
const.dl.response_msg_type = 'LtiDeepLinkingResponse'
const.rl = _const()
const.rl.msg_type = 'LtiResourceLinkRequest'
const.cnav = _const()
const.cnav.msg_type = 'ContextLaunchRequest'
const.subreview = _const()
const.subreview.msg_type = 'LtiSubmissionReviewRequest'
