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
# Generated code. DO NOT EDIT!
#
# Snippet for ReadFeatureValues
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_generated_aiplatform_v1_FeaturestoreOnlineServingService_ReadFeatureValues_sync]
from google.cloud import aiplatform_v1


def sample_read_feature_values():
    """Snippet for read_feature_values"""

    # Create a client
    client = aiplatform_v1.FeaturestoreOnlineServingServiceClient()

    # Initialize request argument(s)
    feature_selector = aiplatform_v1.FeatureSelector()
    feature_selector.id_matcher.ids = ['ids_value_1', 'ids_value_2']

    request = aiplatform_v1.ReadFeatureValuesRequest(
        entity_type="projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}",
        entity_id="entity_id_value",
        feature_selector=feature_selector,
    )

    # Make the request
    response = client.read_feature_values(request=request)

    # Handle response
    print(response)

# [END aiplatform_generated_aiplatform_v1_FeaturestoreOnlineServingService_ReadFeatureValues_sync]
