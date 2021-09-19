from datetime import date, datetime

import requests


def str_to_date(string: str):
    stamp = int(string.strip("/")[5:15])
    return datetime.fromtimestamp(stamp)


class Next_services:

    REAL_TIME_API = "http://realtime.adelaidemetro.com.au/sirism/SiriStopMonitoring.svc/json/SM?MonitoringRef="

    def __init__(self, stop_code):

        self.next_services = list()
        self.stop_code = stop_code
        self.real_time_data = self._check_real_time()
        self._build_next_services()

    def _check_real_time(self):
        try:
            r = requests.get(f"{self.REAL_TIME_API}{self.stop_code}")
            data = r.json()

            return data
        except Exception as e:
            print(e)

    def _arrives_in(self, arrival_time: datetime):
        now = datetime.now()
        at = arrival_time
        here_in = int((at - now).seconds / 60)
        return f"{here_in} min" if here_in > 1 else "now"

    def track_bus(self, route: str):

        arr = self.next_services

        sub = filter(lambda x: x["route"] == route, arr)
        return list(sub)

    def _build_next_services(self):

        next_services_response = self.real_time_data["StopMonitoringDelivery"][0].get(
            "MonitoredStopVisit"
        )
        if not next_services_response:
            return

        for next_service in next_services_response:
            ns_data = dict()
            recorded_time = str_to_date(next_service["RecordedAtTime"])
            destination_time = str_to_date(
                next_service["MonitoredVehicleJourney"]["DestinationAimedArrivalTime"]
            )
            aimed_time = str_to_date(
                next_service["MonitoredVehicleJourney"]["MonitoredCall"][
                    "AimedArrivalTime"
                ]
            )
            expected_time = str_to_date(
                next_service["MonitoredVehicleJourney"]["MonitoredCall"][
                    "LatestExpectedArrivalTime"
                ]
            )
            ns_data["recorded_at"] = recorded_time
            ns_data["journey_code"] = next_service["MonitoredVehicleJourney"][
                "BlockRef"
            ]["Value"]
            ns_data["destination_time"] = destination_time
            ns_data["destination"] = next_service["MonitoredVehicleJourney"][
                "DestinationName"
            ][0]["Value"]
            ns_data["direction"] = next_service["MonitoredVehicleJourney"][
                "DirectionRef"
            ]["Value"]
            ns_data["trip_id"] = next_service["MonitoredVehicleJourney"][
                "FramedVehicleJourneyRef"
            ]["DatedVehicleJourneyRef"]
            ns_data["route"] = next_service["MonitoredVehicleJourney"]["LineRef"][
                "Value"
            ]
            ns_data["stop_name"] = next_service["MonitoredVehicleJourney"][
                "MonitoredCall"
            ]["StopPointName"][0]["Value"]
            ns_data["stop_code"] = next_service["MonitoredVehicleJourney"][
                "MonitoredCall"
            ]["StopPointRef"]["Value"]
            ns_data["aimed_time"] = aimed_time
            ns_data["expected_time"] = expected_time
            ns_data["arrives_in"] = self._arrives_in(expected_time)
            ns_data["vehicle_location"] = [
                float(
                    next_service["MonitoredVehicleJourney"]["VehicleLocation"]["Items"][
                        1
                    ]
                ),
                float(
                    next_service["MonitoredVehicleJourney"]["VehicleLocation"]["Items"][
                        0
                    ]
                ),
            ]

            self.next_services.append(ns_data)
