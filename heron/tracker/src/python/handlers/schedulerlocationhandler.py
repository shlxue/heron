# Copyright 2016 Twitter. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tornado.gen
import tornado.web
import traceback

from heron.tracker.src.python import constants
from heron.tracker.src.python.handlers import BaseHandler

class SchedulerLocationHandler(BaseHandler):
  """
  URL - /topologies/schedulerlocation
  Parameters:
   - cluster (required)
   - environ (required)
   - topology (required) name of the requested topology

  The response JSON is a dictionary with all the
  information of scheduler location of the topology.
  """

  def initialize(self, tracker):
    self.tracker = tracker

  @tornado.gen.coroutine
  def get(self):
    try:
      cluster = self.get_argument_cluster()
      environ = self.get_argument_environ()
      topology_name = self.get_argument_topology()
      topology_info = self.tracker.getTopologyInfo(topology_name, cluster, environ)
      scheduler_location = topology_info["scheduler_location"]
      self.write_success_response(scheduler_location)
    except Exception as e:
      traceback.print_exc()
      self.write_error_response(e)

