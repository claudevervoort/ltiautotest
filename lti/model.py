models = {
    'Context': {
        'id': [],
        'title': [],
        'label': [],
        'type': ['', 'List[str]']
    },
    'ResourceLink': {
        'id': [],
        'title': [],
        'description':[]
    },
    'ToolPlatform': {
    },
    'LaunchPresentation': {
    },
    'Custom': {},
    'DeeplinkSettings': {
        'return_url': ["deep_link_return_url"],
        "accept_types": ['', 'List[str]'],
        "accept_media_types": ['', 'List[str]'],
        "accept_presentation_document_targets": ['', 'List[str]'],
        "accept_multiple": ['', 'bool'],
        "accept_lineitem": ['', 'bool'],
        "auto_create": ['', 'bool'],
        "title": [],
        "text": [],
        "data": []
    },
    'GradeService': {
        'lineitem': [],
        'lineitems': [],
        'scope':['', 'List[str]']
    },
    'MembershipService': {
        'context_memberships_url': [],
        'service_version': []
    },
    'User': {
        'user_id': [],
        'person_sourcedid': [],
        'given_name': [],
        'family_name': [],
        'name': [],
        'email': []
    },
    'LTIMessage': {
        "iss": [],
        "sub": [],
        "given_name": [],
        "family_name": [],
        "name": [],
        "email": [],
        "lti_launch_id": ["https://purl.imsglobal.org/spec/lti/claim/lti_launch_id"],
        "deployment_id": ["https://purl.imsglobal.org/spec/lti/claim/deployment_id"],
        "target_link_uri": ["https://purl.imsglobal.org/spec/lti/claim/target_link_uri"],
        "message_type": ["https://purl.imsglobal.org/spec/lti/claim/message_type"],
        "version": ["https://purl.imsglobal.org/spec/lti/claim/version"],
        "role": ["https://purl.imsglobal.org/spec/lti/claim/roles", "List[str]"],
        "context": ["https://purl.imsglobal.org/spec/lti/claim/context", 'Context'],
        "resource_link": ["https://purl.imsglobal.org/spec/lti/claim/resource_link", 'ResourceLink'],
        "tool_platform": ["https://purl.imsglobal.org/spec/lti/claim/tool_platform", 'ToolPlatform'],
        "launch_presentation": ["https://purl.imsglobal.org/spec/lti/claim/launch_presentation", 'LaunchPresentation'],
        "custom": ["https://purl.imsglobal.org/spec/lti/claim/custom", 'Custom'],
        "deep_linking_settings": ["https://purl.imsglobal.org/spec/lti-dl/claim/deep_linking_settings", 'DeeplinkSettings'],
        "grade_service": ['https://purl.imsglobal.org/spec/lti-ags/claim/endpoint', 'GradeService'],
        "membership_service": ["https://purl.imsglobal.org/spec/lti-nrps/claim/namesroleservice", 'MembershipService'],
        "for_user": ["https://purl.imsglobal.org/spec/lti/claim/for_user", 'User']
    },
    'DeeplinkResponse': {
        "version": ["https://purl.imsglobal.org/spec/lti/claim/version", "str", "1.3.0"],
        "message_type": ["https://purl.imsglobal.org/spec/lti/claim/message_type", "str", "LtiDeepLinkingResponse"],
        "data": ["https://purl.imsglobal.org/spec/lti-dl/claim/data"],
        "deployment_id": ["https://purl.imsglobal.org/spec/lti/claim/deployment_id"],
        "content_items": ["https://purl.imsglobal.org/spec/lti-dl/claim/content_items", "List"]
    },
    'SubmissionReview': {
        'label': [],
        'url': [],
        'custom': ['', 'Custom']
    },
    'LineItem': {
        'cls_const': {
            'mime': 'application/vnd.ims.lis.v2.lineitem+json',
            'mime_collection': 'application/vnd.ims.lis.v2.lineitemcontainer+json',
            'read_scope': 'https://purl.imsglobal.org/spec/lti-ags/scope/lineitem.readonly',
            'write_scope': 'https://purl.imsglobal.org/spec/lti-ags/scope/lineitem'
        },
        'id': [],
        'label': [],
        'scoreMaximum': ['', 'float'],
        'tag': [],
        'submissionReview': ['', 'SubmissionReview'],
        'resourceId': [],
        'resourceLinkId': [],
        'startDateTime': [],
        'endDateTime': [],
    },
    'GradingProgress': (
        'NotReady',
        'Failed',
        'Pending',
        'PendingManual',
        'FullyGraded'
    ),
    'ActivityProgress' : (
        'Initialized',
        'Started',
        'InProgress',
        'Submitted',
        'Completed'
    ),
    'Score': {
        'cls_const': {
            'mime': 'application/vnd.ims.lis.v1.score+json',
            'write_scope': 'https://purl.imsglobal.org/spec/lti-ags/scope/score',
            'path_suffix': 'scores'
        },
        'userId': [],
        'scoreGiven': ['', 'float'],
        'scoreMaximum': ['', 'float'],
        'comment': [],
        'timestamp': ['', 'datetime'],
        'activityProgress': ['', 'ActivityProgress'],
        'gradingProgress': ['', 'GradingProgress']
    },
    'Result': {
        'cls_const': {
            'mime': 'application/vnd.ims.lis.v2.resultcontainer+json',
            'read_scope': 'https://purl.imsglobal.org/spec/lti-ags/scope/result.readonly',
            'path_suffix': 'results'
        },
        'userId': [],
        'resultScore': ['', 'float'],
        'resultMaximum': ['', 'float'],
        'comment': [],
        'timestamp': [],
    },
    'DLIFrame': {
        'width': ['', 'float'],
        'height': ['', 'float']
    },
    'DLWindow': {
        'targetName': []
    },
    'TimeSpan': {
        'startDateTime': [],
        'endDateTime': []
    },
    'LTIResourceLink': {
        'type': ['', 'str', 'ltiResourceLink'],
        'title': [],
        'text': [],
        'url': [],
        'custom': ['', 'Dict[str,str]'],
        'line_item': ['lineItem', 'LineItem'],
        'max_points': ['lineItem:LineItem->scoreMaximum', 'float'],
        'resource_id': ['lineItem:LineItem->resourceId', 'str'],
        'tag': ['lineItem:LineItem->tag', 'str'],
        'available': ['', 'TimeSpan'],
        'submission': ['', 'TimeSpan'],
        'iframe': ['', 'DLIFrame'],
        'window': ['', 'DLWindow']
    },
    'DLHTMLFragment': {
        'type': ['', 'str', 'html'],
        'title': [],
        'text': [],
        'html': []
    },
    'DLImage': {
        'type': ['', 'str', 'image'],
        'title': [],
        'text': [],
        'url': [],
        'width': ['', 'float'],
        'height': ['', 'float']
    },
    'MemberStatus': ('Active', 'Inactive', 'Deleted'),
    'Member': {
        'status': ['', 'MemberStatus'],
        'context_id': [],
        'context_label': [],
        'context_title': [],
        'name': [],
        'picture': [],
        'given_name': [],
        'family_name': [],
        'middle_name': [],
        'email': [],
        'user_id': [],
        'roles': ['', 'List[str]']
    },
    'Members': {
        'cls_const': {
            'mime': 'application/vnd.ims.lti-nrps.v2.membershipcontainer+json',
            'read_scope': 'https://purl.imsglobal.org/spec/lti-nrps/scope/contextmembership.readonly',
            'collection_attribute': 'members'
        },
        'id': [],
        'members': ['', 'List[Member]']
    },
    'SupportedMessage': {
        'type': [],
        'placements': ['', 'List[str]']
    },
    'PlatformConfig': {
        'product_family_code': [],
        'variables': ['', 'List[str]'],
        'messages_supported': ['', 'List[SupportedMessage]'],
    },
    'PlatformOIDCConfig': {
        'issuer': [],
        'authorization_endpoint': [],
        'token_endpoint': [],
        'token_endpoint_auth_methods_supported': ['', 'List[str]'],
        'token_endpoint_auth_signing_alg_values_supported': ['', 'List[str]'],
        'jwks_uri': [],
        'registration_endpoint': [],
        'scopes_supported': ['', 'List[str]'],
        'response_types_supported': ['', 'List[str]'],
        'subject_types_supported': ['', 'List[str]'],
        'id_token_signing_alg_values_supported': ['', 'List[str]'],
        'claims_supported': ['', 'List[str]'],
        'lti_config': ['https://purl.imsglobal.org/spec/lti-platform-configuration', 'PlatformConfig']
    },
    'MessageDef': {
        "type": [],
        "target_link_uri": [],
        "label": [],
        "custom_parameters": ['', 'Custom'],
        "placements": ['', 'List[str]'],
        "roles": ['', 'List[str]']
    },
    'Oauth11Consumer': {
        "key": [],
        "nonce": [],
        "sign": []
    },
    'ToolConfig': {
        "version": [],
        "domain": [],
        "description": [],
        "oauth_consumer": ['', 'Oauth11Consumer'],
        "target_link_uri": [],
        "custom_parameters": ['', 'Custom'],
        "scopes": ['', 'List[str]'],
        "claims": ['', 'List[str]'],
        "messages": ['', 'List[MessageDef]'],
    },
    'ToolOIDCConfig': {
        "client_id": [],
        "registration_client_uri": [],
        "application_type": [],
        "response_types": ['', 'List[str]'],
        "grant_types": ['', 'List[str]'],
        "initiate_login_uri": [],
        "redirect_uris": ['', 'List[str]'],
        "client_name": [],
        "jwks_uri": [],
        "logo_uri": [],
        "token_endpoint_auth_method": [],
        "contacts": ['', 'List[str]'],
        "scope": [],
        "lti_config": ["https://purl.imsglobal.org/spec/lti-tool-configuration", 'ToolConfig']
    }
}
