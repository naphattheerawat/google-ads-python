# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/managed_placement_view_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import managed_placement_view_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_managed__placement__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/managed_placement_view_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v0.servicesB ManagedPlacementViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services\352\002$Google::Ads::GoogleAds::V0::Services'),
  serialized_pb=_b('\nKgoogle/ads/googleads_v0/proto/services/managed_placement_view_service.proto\x12 google.ads.googleads.v0.services\x1a\x44google/ads/googleads_v0/proto/resources/managed_placement_view.proto\x1a\x1cgoogle/api/annotations.proto\"7\n\x1eGetManagedPlacementViewRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xf5\x01\n\x1bManagedPlacementViewService\x12\xd5\x01\n\x17GetManagedPlacementView\x12@.google.ads.googleads.v0.services.GetManagedPlacementViewRequest\x1a\x37.google.ads.googleads.v0.resources.ManagedPlacementView\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/v0/{resource_name=customers/*/managedPlacementViews/*}B\x87\x02\n$com.google.ads.googleads.v0.servicesB ManagedPlacementViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Services\xea\x02$Google::Ads::GoogleAds::V0::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_managed__placement__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETMANAGEDPLACEMENTVIEWREQUEST = _descriptor.Descriptor(
  name='GetManagedPlacementViewRequest',
  full_name='google.ads.googleads.v0.services.GetManagedPlacementViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetManagedPlacementViewRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=213,
  serialized_end=268,
)

DESCRIPTOR.message_types_by_name['GetManagedPlacementViewRequest'] = _GETMANAGEDPLACEMENTVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetManagedPlacementViewRequest = _reflection.GeneratedProtocolMessageType('GetManagedPlacementViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETMANAGEDPLACEMENTVIEWREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.managed_placement_view_service_pb2'
  ,
  __doc__ = """Request message for
  [ManagedPlacementViewService.GetManagedPlacementView][google.ads.googleads.v0.services.ManagedPlacementViewService.GetManagedPlacementView].
  
  
  Attributes:
      resource_name:
          The resource name of the Managed Placement View to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetManagedPlacementViewRequest)
  ))
_sym_db.RegisterMessage(GetManagedPlacementViewRequest)


DESCRIPTOR._options = None

_MANAGEDPLACEMENTVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='ManagedPlacementViewService',
  full_name='google.ads.googleads.v0.services.ManagedPlacementViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=271,
  serialized_end=516,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetManagedPlacementView',
    full_name='google.ads.googleads.v0.services.ManagedPlacementViewService.GetManagedPlacementView',
    index=0,
    containing_service=None,
    input_type=_GETMANAGEDPLACEMENTVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_managed__placement__view__pb2._MANAGEDPLACEMENTVIEW,
    serialized_options=_b('\202\323\344\223\0029\0227/v0/{resource_name=customers/*/managedPlacementViews/*}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MANAGEDPLACEMENTVIEWSERVICE)

DESCRIPTOR.services_by_name['ManagedPlacementViewService'] = _MANAGEDPLACEMENTVIEWSERVICE

# @@protoc_insertion_point(module_scope)