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
from google.cloud.dataplex_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.content_service import ContentServiceAsyncClient, ContentServiceClient
from .services.data_scan_service import (
    DataScanServiceAsyncClient,
    DataScanServiceClient,
)
from .services.dataplex_service import DataplexServiceAsyncClient, DataplexServiceClient
from .services.metadata_service import MetadataServiceAsyncClient, MetadataServiceClient
from .types.analyze import Content, Environment, Session
from .types.content import (
    CreateContentRequest,
    DeleteContentRequest,
    GetContentRequest,
    ListContentRequest,
    ListContentResponse,
    UpdateContentRequest,
)
from .types.data_profile import DataProfileResult, DataProfileSpec
from .types.data_quality import (
    DataQualityDimensionResult,
    DataQualityResult,
    DataQualityRule,
    DataQualityRuleResult,
    DataQualitySpec,
)
from .types.datascans import (
    CreateDataScanRequest,
    DataScan,
    DataScanJob,
    DataScanType,
    DeleteDataScanRequest,
    GetDataScanJobRequest,
    GetDataScanRequest,
    ListDataScanJobsRequest,
    ListDataScanJobsResponse,
    ListDataScansRequest,
    ListDataScansResponse,
    RunDataScanRequest,
    RunDataScanResponse,
    UpdateDataScanRequest,
)
from .types.logs import DataScanEvent, DiscoveryEvent, JobEvent, SessionEvent
from .types.metadata_ import (
    CreateEntityRequest,
    CreatePartitionRequest,
    DeleteEntityRequest,
    DeletePartitionRequest,
    Entity,
    GetEntityRequest,
    GetPartitionRequest,
    ListEntitiesRequest,
    ListEntitiesResponse,
    ListPartitionsRequest,
    ListPartitionsResponse,
    Partition,
    Schema,
    StorageAccess,
    StorageFormat,
    StorageSystem,
    UpdateEntityRequest,
)
from .types.processing import DataSource, ScannedData, Trigger
from .types.resources import Action, Asset, AssetStatus, Lake, State, Zone
from .types.service import (
    CancelJobRequest,
    CreateAssetRequest,
    CreateEnvironmentRequest,
    CreateLakeRequest,
    CreateTaskRequest,
    CreateZoneRequest,
    DeleteAssetRequest,
    DeleteEnvironmentRequest,
    DeleteLakeRequest,
    DeleteTaskRequest,
    DeleteZoneRequest,
    GetAssetRequest,
    GetEnvironmentRequest,
    GetJobRequest,
    GetLakeRequest,
    GetTaskRequest,
    GetZoneRequest,
    ListActionsResponse,
    ListAssetActionsRequest,
    ListAssetsRequest,
    ListAssetsResponse,
    ListEnvironmentsRequest,
    ListEnvironmentsResponse,
    ListJobsRequest,
    ListJobsResponse,
    ListLakeActionsRequest,
    ListLakesRequest,
    ListLakesResponse,
    ListSessionsRequest,
    ListSessionsResponse,
    ListTasksRequest,
    ListTasksResponse,
    ListZoneActionsRequest,
    ListZonesRequest,
    ListZonesResponse,
    OperationMetadata,
    RunTaskRequest,
    RunTaskResponse,
    UpdateAssetRequest,
    UpdateEnvironmentRequest,
    UpdateLakeRequest,
    UpdateTaskRequest,
    UpdateZoneRequest,
)
from .types.tasks import Job, Task

__all__ = (
    "ContentServiceAsyncClient",
    "DataScanServiceAsyncClient",
    "DataplexServiceAsyncClient",
    "MetadataServiceAsyncClient",
    "Action",
    "Asset",
    "AssetStatus",
    "CancelJobRequest",
    "Content",
    "ContentServiceClient",
    "CreateAssetRequest",
    "CreateContentRequest",
    "CreateDataScanRequest",
    "CreateEntityRequest",
    "CreateEnvironmentRequest",
    "CreateLakeRequest",
    "CreatePartitionRequest",
    "CreateTaskRequest",
    "CreateZoneRequest",
    "DataProfileResult",
    "DataProfileSpec",
    "DataQualityDimensionResult",
    "DataQualityResult",
    "DataQualityRule",
    "DataQualityRuleResult",
    "DataQualitySpec",
    "DataScan",
    "DataScanEvent",
    "DataScanJob",
    "DataScanServiceClient",
    "DataScanType",
    "DataSource",
    "DataplexServiceClient",
    "DeleteAssetRequest",
    "DeleteContentRequest",
    "DeleteDataScanRequest",
    "DeleteEntityRequest",
    "DeleteEnvironmentRequest",
    "DeleteLakeRequest",
    "DeletePartitionRequest",
    "DeleteTaskRequest",
    "DeleteZoneRequest",
    "DiscoveryEvent",
    "Entity",
    "Environment",
    "GetAssetRequest",
    "GetContentRequest",
    "GetDataScanJobRequest",
    "GetDataScanRequest",
    "GetEntityRequest",
    "GetEnvironmentRequest",
    "GetJobRequest",
    "GetLakeRequest",
    "GetPartitionRequest",
    "GetTaskRequest",
    "GetZoneRequest",
    "Job",
    "JobEvent",
    "Lake",
    "ListActionsResponse",
    "ListAssetActionsRequest",
    "ListAssetsRequest",
    "ListAssetsResponse",
    "ListContentRequest",
    "ListContentResponse",
    "ListDataScanJobsRequest",
    "ListDataScanJobsResponse",
    "ListDataScansRequest",
    "ListDataScansResponse",
    "ListEntitiesRequest",
    "ListEntitiesResponse",
    "ListEnvironmentsRequest",
    "ListEnvironmentsResponse",
    "ListJobsRequest",
    "ListJobsResponse",
    "ListLakeActionsRequest",
    "ListLakesRequest",
    "ListLakesResponse",
    "ListPartitionsRequest",
    "ListPartitionsResponse",
    "ListSessionsRequest",
    "ListSessionsResponse",
    "ListTasksRequest",
    "ListTasksResponse",
    "ListZoneActionsRequest",
    "ListZonesRequest",
    "ListZonesResponse",
    "MetadataServiceClient",
    "OperationMetadata",
    "Partition",
    "RunDataScanRequest",
    "RunDataScanResponse",
    "RunTaskRequest",
    "RunTaskResponse",
    "ScannedData",
    "Schema",
    "Session",
    "SessionEvent",
    "State",
    "StorageAccess",
    "StorageFormat",
    "StorageSystem",
    "Task",
    "Trigger",
    "UpdateAssetRequest",
    "UpdateContentRequest",
    "UpdateDataScanRequest",
    "UpdateEntityRequest",
    "UpdateEnvironmentRequest",
    "UpdateLakeRequest",
    "UpdateTaskRequest",
    "UpdateZoneRequest",
    "Zone",
)
