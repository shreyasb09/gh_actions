
from ieg.managers.costmanager import CostManager
from ieg.models.aws.ce import (
    TimePeriod,
    Filter,
)
from ieg.utils import load_yaml
from typing import Any
from datetime import datetime
from pathlib import Path
from ieg.aws.s3 import S3
from ieg.managers.kubecost import KubeCostManager
from ieg.aws.secretmanager import SecretManager
from ieg.api.kubecostapi import KubecostAPI


# def _get_window_duration(time_period: TimePeriod) -> int:
#     """
#     Given a time period with start and end dates, returns the duration of the window in days.

#     Args:
#         time_period (TimePeriod): A named tuple containing the start and end dates as ISO 8601 strings.

#     Returns:
#         int: The number of days in the time window, inclusive.
#     """
#     start_date = datetime.fromisoformat(time_period.start).date()
#     end_date = datetime.fromisoformat(time_period.end).date()
#     duration = (end_date - start_date).days + 1
#     return duration


# all_known_stacks: dict[str, Any] = load_yaml(yaml_path="cpcost.yml")
# eks_cluster_stacks: dict[str, list[str]] = {}
# regions_list: list[str] = []
# for region, stacks in all_known_stacks.items():
#     regions_list.append(region)
#     eks_cluster_stacks[region] = eks_cluster_stacks.get(region, [])
#     if stacks is None:
#         continue
#     for stackname, attributes in stacks.items():
#         if attributes.get("InfraType") == "EKS":
#             eks_cluster_stacks[region].append(stackname)


working_dir_name: str = datetime.now().strftime("%Y%m%d%H%M%S")
path = Path(working_dir_name)
path.parent.mkdir(parents=True, exist_ok=True)

# use1: dict[str, list[str]] = {"us-east-1": ["aws-use1-cprod-muse1"]}
# kc = KubeCostManager(working_dir=working_dir_name, window=3, all_known_stacks=use1)
# kc.get_regions_stacks_allocations_cost(kubecost_stacks=use1)
# kc.get_region_stacks_cloud_cost(kubecost_stacks=use1)


granularity = "DAILY"
# window: int = _get_window_duration(time_period=timeperiod)

cm = CostManager(
    working_dir=working_dir_name, window=5, all_known_stacks=[], granularity=granularity
)
cm.write_serviceinfos_csv(regions=["us-east-1", "us-west-2"])

# cm.write_timegrouped_serviceinfos(
#     cost_category="serviceinfo",
#     regions=regions_list,
# )
# cm.write_timegrouped_serviceinfos(
#     cost_category="noTagStack",
#     regions=regions_list,
#     filters=Filter.NO_TAG_KEY_STACK,
# )
# cm.write_timegrouped_stackinfos(
#     regions=regions_list,
# )
# cm.write_timegrouped_nodeInfo(
#     region_known_eks_stacks=eks_cluster_stacks,
# )

# S3().upload_to_s3(
#     local_path=working_dir_name,
#     bucket="iota-athena-bucket",
#     s3_path="cost/data/cloudport/",
# )
