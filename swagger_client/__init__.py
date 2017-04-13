# coding: utf-8

"""
    Veritas Information Classifier (VIC)

    APIs

    OpenAPI spec version: Resource Specific
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.allowed_value import AllowedValue
from .models.error_response import ErrorResponse
from .models.json_patch_document import JsonPatchDocument
from .models.link import Link
from .models.metadata_definition import MetadataDefinition
from .models.metadata_definition_collection import MetadataDefinitionCollection
from .models.node import Node
from .models.operator_node import OperatorNode
from .models.pattern import Pattern
from .models.pattern_collection import PatternCollection
from .models.policy import Policy
from .models.policy_body import PolicyBody
from .models.policy_collection import PolicyCollection
from .models.tag import Tag
from .models.tag_property import TagProperty
from .models.tag_property_allowed_value import TagPropertyAllowedValue
from .models.tag_property_definition import TagPropertyDefinition
from .models.tag_property_definition_collection import TagPropertyDefinitionCollection
from .models.tags_collection import TagsCollection

# import apis into sdk package
from .apis.veritas_information_classifier_vic_api import VeritasInformationClassifierVICApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
