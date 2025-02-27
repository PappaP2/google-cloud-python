# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
import warnings

from google.api_core import gapic_v1, grpc_helpers_async
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.recaptchaenterprise_v1.types import recaptchaenterprise

from .base import DEFAULT_CLIENT_INFO, RecaptchaEnterpriseServiceTransport
from .grpc import RecaptchaEnterpriseServiceGrpcTransport


class RecaptchaEnterpriseServiceGrpcAsyncIOTransport(
    RecaptchaEnterpriseServiceTransport
):
    """gRPC AsyncIO backend transport for RecaptchaEnterpriseService.

    Service to determine the likelihood an event is legitimate.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "recaptchaenterprise.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "recaptchaenterprise.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[aio.Channel] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def create_assessment(
        self,
    ) -> Callable[
        [recaptchaenterprise.CreateAssessmentRequest],
        Awaitable[recaptchaenterprise.Assessment],
    ]:
        r"""Return a callable for the create assessment method over gRPC.

        Creates an Assessment of the likelihood an event is
        legitimate.

        Returns:
            Callable[[~.CreateAssessmentRequest],
                    Awaitable[~.Assessment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_assessment" not in self._stubs:
            self._stubs["create_assessment"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/CreateAssessment",
                request_serializer=recaptchaenterprise.CreateAssessmentRequest.serialize,
                response_deserializer=recaptchaenterprise.Assessment.deserialize,
            )
        return self._stubs["create_assessment"]

    @property
    def annotate_assessment(
        self,
    ) -> Callable[
        [recaptchaenterprise.AnnotateAssessmentRequest],
        Awaitable[recaptchaenterprise.AnnotateAssessmentResponse],
    ]:
        r"""Return a callable for the annotate assessment method over gRPC.

        Annotates a previously created Assessment to provide
        additional information on whether the event turned out
        to be authentic or fraudulent.

        Returns:
            Callable[[~.AnnotateAssessmentRequest],
                    Awaitable[~.AnnotateAssessmentResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "annotate_assessment" not in self._stubs:
            self._stubs["annotate_assessment"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/AnnotateAssessment",
                request_serializer=recaptchaenterprise.AnnotateAssessmentRequest.serialize,
                response_deserializer=recaptchaenterprise.AnnotateAssessmentResponse.deserialize,
            )
        return self._stubs["annotate_assessment"]

    @property
    def create_key(
        self,
    ) -> Callable[
        [recaptchaenterprise.CreateKeyRequest], Awaitable[recaptchaenterprise.Key]
    ]:
        r"""Return a callable for the create key method over gRPC.

        Creates a new reCAPTCHA Enterprise key.

        Returns:
            Callable[[~.CreateKeyRequest],
                    Awaitable[~.Key]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_key" not in self._stubs:
            self._stubs["create_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/CreateKey",
                request_serializer=recaptchaenterprise.CreateKeyRequest.serialize,
                response_deserializer=recaptchaenterprise.Key.deserialize,
            )
        return self._stubs["create_key"]

    @property
    def list_keys(
        self,
    ) -> Callable[
        [recaptchaenterprise.ListKeysRequest],
        Awaitable[recaptchaenterprise.ListKeysResponse],
    ]:
        r"""Return a callable for the list keys method over gRPC.

        Returns the list of all keys that belong to a
        project.

        Returns:
            Callable[[~.ListKeysRequest],
                    Awaitable[~.ListKeysResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_keys" not in self._stubs:
            self._stubs["list_keys"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/ListKeys",
                request_serializer=recaptchaenterprise.ListKeysRequest.serialize,
                response_deserializer=recaptchaenterprise.ListKeysResponse.deserialize,
            )
        return self._stubs["list_keys"]

    @property
    def retrieve_legacy_secret_key(
        self,
    ) -> Callable[
        [recaptchaenterprise.RetrieveLegacySecretKeyRequest],
        Awaitable[recaptchaenterprise.RetrieveLegacySecretKeyResponse],
    ]:
        r"""Return a callable for the retrieve legacy secret key method over gRPC.

        Returns the secret key related to the specified
        public key. You must use the legacy secret key only in a
        3rd party integration with legacy reCAPTCHA.

        Returns:
            Callable[[~.RetrieveLegacySecretKeyRequest],
                    Awaitable[~.RetrieveLegacySecretKeyResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "retrieve_legacy_secret_key" not in self._stubs:
            self._stubs["retrieve_legacy_secret_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/RetrieveLegacySecretKey",
                request_serializer=recaptchaenterprise.RetrieveLegacySecretKeyRequest.serialize,
                response_deserializer=recaptchaenterprise.RetrieveLegacySecretKeyResponse.deserialize,
            )
        return self._stubs["retrieve_legacy_secret_key"]

    @property
    def get_key(
        self,
    ) -> Callable[
        [recaptchaenterprise.GetKeyRequest], Awaitable[recaptchaenterprise.Key]
    ]:
        r"""Return a callable for the get key method over gRPC.

        Returns the specified key.

        Returns:
            Callable[[~.GetKeyRequest],
                    Awaitable[~.Key]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_key" not in self._stubs:
            self._stubs["get_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/GetKey",
                request_serializer=recaptchaenterprise.GetKeyRequest.serialize,
                response_deserializer=recaptchaenterprise.Key.deserialize,
            )
        return self._stubs["get_key"]

    @property
    def update_key(
        self,
    ) -> Callable[
        [recaptchaenterprise.UpdateKeyRequest], Awaitable[recaptchaenterprise.Key]
    ]:
        r"""Return a callable for the update key method over gRPC.

        Updates the specified key.

        Returns:
            Callable[[~.UpdateKeyRequest],
                    Awaitable[~.Key]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_key" not in self._stubs:
            self._stubs["update_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/UpdateKey",
                request_serializer=recaptchaenterprise.UpdateKeyRequest.serialize,
                response_deserializer=recaptchaenterprise.Key.deserialize,
            )
        return self._stubs["update_key"]

    @property
    def delete_key(
        self,
    ) -> Callable[[recaptchaenterprise.DeleteKeyRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete key method over gRPC.

        Deletes the specified key.

        Returns:
            Callable[[~.DeleteKeyRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_key" not in self._stubs:
            self._stubs["delete_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/DeleteKey",
                request_serializer=recaptchaenterprise.DeleteKeyRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_key"]

    @property
    def migrate_key(
        self,
    ) -> Callable[
        [recaptchaenterprise.MigrateKeyRequest], Awaitable[recaptchaenterprise.Key]
    ]:
        r"""Return a callable for the migrate key method over gRPC.

        Migrates an existing key from reCAPTCHA to reCAPTCHA
        Enterprise. Once a key is migrated, it can be used from
        either product. SiteVerify requests are billed as
        CreateAssessment calls. You must be authenticated as one
        of the current owners of the reCAPTCHA Site Key, and
        your user must have the reCAPTCHA Enterprise Admin IAM
        role in the destination project.

        Returns:
            Callable[[~.MigrateKeyRequest],
                    Awaitable[~.Key]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "migrate_key" not in self._stubs:
            self._stubs["migrate_key"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/MigrateKey",
                request_serializer=recaptchaenterprise.MigrateKeyRequest.serialize,
                response_deserializer=recaptchaenterprise.Key.deserialize,
            )
        return self._stubs["migrate_key"]

    @property
    def get_metrics(
        self,
    ) -> Callable[
        [recaptchaenterprise.GetMetricsRequest], Awaitable[recaptchaenterprise.Metrics]
    ]:
        r"""Return a callable for the get metrics method over gRPC.

        Get some aggregated metrics for a Key. This data can
        be used to build dashboards.

        Returns:
            Callable[[~.GetMetricsRequest],
                    Awaitable[~.Metrics]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_metrics" not in self._stubs:
            self._stubs["get_metrics"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/GetMetrics",
                request_serializer=recaptchaenterprise.GetMetricsRequest.serialize,
                response_deserializer=recaptchaenterprise.Metrics.deserialize,
            )
        return self._stubs["get_metrics"]

    @property
    def list_related_account_groups(
        self,
    ) -> Callable[
        [recaptchaenterprise.ListRelatedAccountGroupsRequest],
        Awaitable[recaptchaenterprise.ListRelatedAccountGroupsResponse],
    ]:
        r"""Return a callable for the list related account groups method over gRPC.

        List groups of related accounts.

        Returns:
            Callable[[~.ListRelatedAccountGroupsRequest],
                    Awaitable[~.ListRelatedAccountGroupsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_related_account_groups" not in self._stubs:
            self._stubs["list_related_account_groups"] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/ListRelatedAccountGroups",
                request_serializer=recaptchaenterprise.ListRelatedAccountGroupsRequest.serialize,
                response_deserializer=recaptchaenterprise.ListRelatedAccountGroupsResponse.deserialize,
            )
        return self._stubs["list_related_account_groups"]

    @property
    def list_related_account_group_memberships(
        self,
    ) -> Callable[
        [recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest],
        Awaitable[recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse],
    ]:
        r"""Return a callable for the list related account group
        memberships method over gRPC.

        Get memberships in a group of related accounts.

        Returns:
            Callable[[~.ListRelatedAccountGroupMembershipsRequest],
                    Awaitable[~.ListRelatedAccountGroupMembershipsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_related_account_group_memberships" not in self._stubs:
            self._stubs[
                "list_related_account_group_memberships"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/ListRelatedAccountGroupMemberships",
                request_serializer=recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest.serialize,
                response_deserializer=recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse.deserialize,
            )
        return self._stubs["list_related_account_group_memberships"]

    @property
    def search_related_account_group_memberships(
        self,
    ) -> Callable[
        [recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest],
        Awaitable[recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse],
    ]:
        r"""Return a callable for the search related account group
        memberships method over gRPC.

        Search group memberships related to a given account.

        Returns:
            Callable[[~.SearchRelatedAccountGroupMembershipsRequest],
                    Awaitable[~.SearchRelatedAccountGroupMembershipsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_related_account_group_memberships" not in self._stubs:
            self._stubs[
                "search_related_account_group_memberships"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseService/SearchRelatedAccountGroupMemberships",
                request_serializer=recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest.serialize,
                response_deserializer=recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse.deserialize,
            )
        return self._stubs["search_related_account_group_memberships"]

    def close(self):
        return self.grpc_channel.close()


__all__ = ("RecaptchaEnterpriseServiceGrpcAsyncIOTransport",)
