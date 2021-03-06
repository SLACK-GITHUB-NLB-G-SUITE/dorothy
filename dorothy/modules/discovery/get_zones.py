#
# Licensed to Elasticsearch under one or more contributor
# license agreements. See the NOTICE file distributed with
# this work for additional information regarding copyright
# ownership. Elasticsearch licenses this file to you under
# the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

# Harvest information on all Okta network zones

import logging.config

import click

from dorothy.core import index_event
from dorothy.modules.discovery.discovery import discovery

LOGGER = logging.getLogger(__name__)
MODULE_DESCRIPTION = "Harvest information on all Okta network zones"
TACTICS = ["Discovery"]


@discovery.subshell(name="get-zones")
@click.pass_context
def get_zones(ctx):
    """Harvest information on all Okta network zones"""


@get_zones.command()
@click.pass_context
def execute(ctx):
    """Execute this module with the configured options"""

    if click.confirm("[*] Do you want to attempt to harvest information on all network zones?", default=True):
        msg = "Attempting to harvest all network zones"
        LOGGER.info(msg)
        index_event(ctx.obj.es, module=__name__, event_type="INFO", event=msg)
        click.echo(f"[*] {msg}")

        ctx.obj.okta.get_zones(ctx)
