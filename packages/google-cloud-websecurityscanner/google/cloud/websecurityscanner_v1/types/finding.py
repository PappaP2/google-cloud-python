# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
import proto  # type: ignore

from google.cloud.websecurityscanner_v1.types import finding_addon


__protobuf__ = proto.module(
    package="google.cloud.websecurityscanner.v1", manifest={"Finding",},
)


class Finding(proto.Message):
    r"""A Finding resource represents a vulnerability instance
    identified during a ScanRun.

    Attributes:
        name (str):
            Output only. The resource name of the
            Finding. The name follows the format of
            'projects/{projectId}/scanConfigs/{scanConfigId}/scanruns/{scanRunId}/findings/{findingId}'.
            The finding IDs are generated by the system.
        finding_type (str):
            Output only. The type of the Finding.
            Detailed and up-to-date information on findings
            can be found here:
            https://cloud.google.com/security-command-
            center/docs/how-to-remediate-web-security-
            scanner-findings
        severity (google.cloud.websecurityscanner_v1.types.Finding.Severity):
            Output only. The severity level of the
            reported vulnerability.
        http_method (str):
            Output only. The http method of the request
            that triggered the vulnerability, in uppercase.
        fuzzed_url (str):
            Output only. The URL produced by the server-
            ide fuzzer and used in the request that
            triggered the vulnerability.
        body (str):
            Output only. The body of the request that
            triggered the vulnerability.
        description (str):
            Output only. The description of the
            vulnerability.
        reproduction_url (str):
            Output only. The URL containing human-
            eadable payload that user can leverage to
            reproduce the vulnerability.
        frame_url (str):
            Output only. If the vulnerability was
            originated from nested IFrame, the immediate
            parent IFrame is reported.
        final_url (str):
            Output only. The URL where the browser lands
            when the vulnerability is detected.
        tracking_id (str):
            Output only. The tracking ID uniquely
            identifies a vulnerability instance across
            multiple ScanRuns.
        form (google.cloud.websecurityscanner_v1.types.Form):
            Output only. An addon containing information
            reported for a vulnerability with an HTML form,
            if any.
        outdated_library (google.cloud.websecurityscanner_v1.types.OutdatedLibrary):
            Output only. An addon containing information
            about outdated libraries.
        violating_resource (google.cloud.websecurityscanner_v1.types.ViolatingResource):
            Output only. An addon containing detailed
            information regarding any resource causing the
            vulnerability such as JavaScript sources, image,
            audio files, etc.
        vulnerable_headers (google.cloud.websecurityscanner_v1.types.VulnerableHeaders):
            Output only. An addon containing information
            about vulnerable or missing HTTP headers.
        vulnerable_parameters (google.cloud.websecurityscanner_v1.types.VulnerableParameters):
            Output only. An addon containing information
            about request parameters which were found to be
            vulnerable.
        xss (google.cloud.websecurityscanner_v1.types.Xss):
            Output only. An addon containing information
            reported for an XSS, if any.
    """

    class Severity(proto.Enum):
        r"""The severity level of a vulnerability."""
        SEVERITY_UNSPECIFIED = 0
        CRITICAL = 1
        HIGH = 2
        MEDIUM = 3
        LOW = 4

    name = proto.Field(proto.STRING, number=1,)
    finding_type = proto.Field(proto.STRING, number=2,)
    severity = proto.Field(proto.ENUM, number=17, enum=Severity,)
    http_method = proto.Field(proto.STRING, number=3,)
    fuzzed_url = proto.Field(proto.STRING, number=4,)
    body = proto.Field(proto.STRING, number=5,)
    description = proto.Field(proto.STRING, number=6,)
    reproduction_url = proto.Field(proto.STRING, number=7,)
    frame_url = proto.Field(proto.STRING, number=8,)
    final_url = proto.Field(proto.STRING, number=9,)
    tracking_id = proto.Field(proto.STRING, number=10,)
    form = proto.Field(proto.MESSAGE, number=16, message=finding_addon.Form,)
    outdated_library = proto.Field(
        proto.MESSAGE, number=11, message=finding_addon.OutdatedLibrary,
    )
    violating_resource = proto.Field(
        proto.MESSAGE, number=12, message=finding_addon.ViolatingResource,
    )
    vulnerable_headers = proto.Field(
        proto.MESSAGE, number=15, message=finding_addon.VulnerableHeaders,
    )
    vulnerable_parameters = proto.Field(
        proto.MESSAGE, number=13, message=finding_addon.VulnerableParameters,
    )
    xss = proto.Field(proto.MESSAGE, number=14, message=finding_addon.Xss,)


__all__ = tuple(sorted(__protobuf__.manifest))
