# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
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
# ==============================================================================
"""FlowerContext and Metadata."""


from dataclasses import dataclass

from .recordset import RecordSet


@dataclass
class Metadata:
    """A dataclass holding metadata associated with the current task.

    Parameters
    ----------
    run_id : int
        An identifier for the current run.
    task_id : str
        An identifier for the current task.
    group_id : str
        An identifier for grouping tasks. In some settings
        this is used as the FL round.
    ttl : str
        Time-to-live for this task.
    task_type : str
        A string that encodes the action to be executed on
        the receiving end.
    """

    run_id: int
    task_id: str
    group_id: str
    ttl: str
    task_type: str


@dataclass
class FlowerContext:
    """State of your application from the viewpoint of the entity using it.

    Parameters
    ----------
    in_message : RecordSet
        Holds records sent by another entity (e.g. sent by the server-side
        logic to a client, or vice-versa)
    out_message : RecordSet
        Holds records added by the current entity. This `RecordSet` will
        be sent out (e.g. back to the server-side for aggregation of
        parameter, or to the client to perform a certain task)
    local : RecordSet
        Holds record added by the current entity and that will stay local.
        This means that the data it holds will never leave the system it's running from.
        This can be used as an intermediate storage or scratchpad when
        executing middleware layers. It can also be used as a memory to access
        at different points during the lifecycle of this entity (e.g. across
        multiple rounds)
    metadata : Metadata
        A dataclass including information about the task to be executed.
    """

    in_message: RecordSet
    out_message: RecordSet
    local: RecordSet
    metadata: Metadata
