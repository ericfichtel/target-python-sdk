# Copyright 2020 Adobe. All rights reserved.
# This file is licensed to you under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy
# of the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
# OF ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

"""Validation functions"""
from target_python_sdk.messages import MESSAGES
from target_python_sdk.enums import DecisioningMethod


def validate_client_options(options):
    """Validates options for TargetClient"""
    if not options:
        return MESSAGES.get('OPTIONS_REQUIRED')

    client, organization_id, decisioning_method = \
        [options.get(k) for k in ('client', 'organization_id', 'decisioning_method')]

    if not client:
        return MESSAGES.get('CLIENT_REQUIRED')

    if not organization_id:
        return MESSAGES.get('ORG_ID_REQUIRED')

    if decisioning_method and decisioning_method not in [e.value for e in DecisioningMethod]:
        return MESSAGES.get('DECISIONING_METHOD_INVALID')

    return None