from datetime import date, datetime

import requests


def str_to_date(string:str ):
    stamp = int(string.strip("/")[5:15])
    return datetime.fromtimestamp(stamp)

class Next_services:

    REAL_TIME_API = "http://realtime.adelaidemetro.com.au/sirism/SiriStopMonitoring.svc/json/SM?MonitoringRef="

    test_data = {
            "StopMonitoringDelivery": [
                {
                "ResponseTimestamp": "/Date(1612349373000+1030)/",
                "Status": True,
                "ValidUntil": "/Date(0)/",
                "MonitoredStopVisit": [
                    {
                    "RecordedAtTime": "/Date(1612349249000+1030)/",
                    "ItemIdentifier": "b829b120-4dea-4867-b02e-296c94865585",
                    "MonitoredVehicleJourney": {
                        "BlockRef": {
                        "Value": "3240"
                        },
                        "ConfidenceLevel": 1,
                        "DestinationAimedArrivalTime": "/Date(1612351800000+1030)/",
                        "DestinationAimedArrivalTimeSpecified": True,
                        "DestinationName": [
                        {
                            "Value": "Port Adelaide"
                        }
                        ],
                        "DirectionRef": {
                        "Value": "O"
                        },
                        "DriverName": "Confidential",
                        "DriverRef": "00000",
                        "FramedVehicleJourneyRef": {
                        "DataFrameRef": {
                            "Value": "2021-02-03"
                        },
                        "DatedVehicleJourneyRef": "648348"
                        },
                        "JourneyPatternRef": {
                        "Value": "32"
                        },
                        "LineRef": {
                        "Value": "230"
                        },
                        "Monitored": True,
                        "MonitoredCall": {
                        "StopPointName": [
                            {
                            "Value": "X1 King William St"
                            }
                        ],
                        "StopPointRef": {
                            "Value": "16281"
                        },
                        "AimedArrivalTime": "/Date(1612349460000+1030)/",
                        "AimedArrivalTimeSpecified": True,
                        "AimedDepartureTime": "/Date(0)/",
                        "AimedLatestPassengerAccessTime": "/Date(0)/",
                        "DestinationDisplay": {
                            "Value": "Port Adelaide"
                        },
                        "EarliestExpectedDepartureTime": "/Date(0)/",
                        "ExpectedLatestPassengerAccessTime": "/Date(0)/",
                        "Item": "/Date(0)/",
                        "Item1": "/Date(0)/",
                        "LatestExpectedArrivalTime": "/Date(1612349517000+1030)/",
                        "LatestExpectedArrivalTimeSpecified": True,
                        "ProvisionalExpectedDepartureTime": "/Date(0)/",
                        "VehicleLocationAtStop": {
                            "Items": ["-34.923921", "138.599433"]
                        }
                        },
                        "MonitoredSpecified": True,
                        "OperatorRef": {
                        "Value": "5 - Adelaide Metro (Torrens Transit)"
                        },
                        "OriginAimedDepartureTime": "/Date(0)/",
                        "VehicleLocation": {
                        "Items": ["-34.931940", "138.6062"]
                        },
                        "VehicleRef": {
                        "Value": "1953"
                        }
                    },
                    "MonitoringRef": {
                        "Value": "16281"
                    },
                    "StopVisitNote": [
                        {
                        "Value": "StopType=BS"
                        }
                    ],
                    "ValidUntilTime": "/Date(0)/"
                    },
                    {
                    "RecordedAtTime": "/Date(1612349034000+1030)/",
                    "ItemIdentifier": "44e3efa8-bd14-4400-aca3-877d538fce95",
                    "MonitoredVehicleJourney": {
                        "BlockRef": {
                        "Value": "368"
                        },
                        "ConfidenceLevel": 1,
                        "DestinationAimedArrivalTime": "/Date(1612352400000+1030)/",
                        "DestinationAimedArrivalTimeSpecified": True,
                        "DestinationName": [
                        {
                            "Value": "Paradise"
                        }
                        ],
                        "DirectionRef": {
                        "Value": "O"
                        },
                        "DriverName": "Confidential",
                        "DriverRef": "00000",
                        "FramedVehicleJourneyRef": {
                        "DataFrameRef": {
                            "Value": "2021-02-03"
                        },
                        "DatedVehicleJourneyRef": "647113"
                        },
                        "JourneyPatternRef": {
                        "Value": "52"
                        },
                        "LineRef": {
                        "Value": "178"
                        },
                        "Monitored": True,
                        "MonitoredCall": {
                        "StopPointName": [
                            {
                            "Value": "X1 King William St"
                            }
                        ],
                        "StopPointRef": {
                            "Value": "16281"
                        },
                        "AimedArrivalTime": "/Date(1612349640000+1030)/",
                        "AimedArrivalTimeSpecified": True,
                        "AimedDepartureTime": "/Date(0)/",
                        "AimedLatestPassengerAccessTime": "/Date(0)/",
                        "DestinationDisplay": {
                            "Value": "Paradise"
                        },
                        "EarliestExpectedDepartureTime": "/Date(0)/",
                        "ExpectedLatestPassengerAccessTime": "/Date(0)/",
                        "Item": "/Date(0)/",
                        "Item1": "/Date(0)/",
                        "LatestExpectedArrivalTime": "/Date(1612349785000+1030)/",
                        "LatestExpectedArrivalTimeSpecified": True,
                        "ProvisionalExpectedDepartureTime": "/Date(0)/",
                        "VehicleLocationAtStop": {
                            "Items": ["-34.923921", "138.599433"]
                        }
                        },
                        "MonitoredSpecified": True,
                        "OperatorRef": {
                        "Value": "5 - Adelaide Metro (Torrens Transit)"
                        },
                        "OriginAimedDepartureTime": "/Date(0)/",
                        "VehicleLocation": {
                        "Items": ["-34.955490", "138.6258"]
                        },
                        "VehicleRef": {
                        "Value": "1801"
                        }
                    },
                    "MonitoringRef": {
                        "Value": "16281"
                    },
                    "StopVisitNote": [
                        {
                        "Value": "StopType=BS"
                        }
                    ],
                    "ValidUntilTime": "/Date(0)/"
                    },
                    {
                    "RecordedAtTime": "/Date(1612349140000+1030)/",
                    "ItemIdentifier": "45544712-1be9-477c-b9e9-c6575aa83556",
                    "MonitoredVehicleJourney": {
                        "BlockRef": {
                        "Value": "3698"
                        },
                        "ConfidenceLevel": 1,
                        "DestinationAimedArrivalTime": "/Date(1612352220000+1030)/",
                        "DestinationAimedArrivalTimeSpecified": True,
                        "DestinationName": [
                        {
                            "Value": "Paradise"
                        }
                        ],
                        "DirectionRef": {
                        "Value": "O"
                        },
                        "DriverName": "Confidential",
                        "DriverRef": "00000",
                        "FramedVehicleJourneyRef": {
                        "DataFrameRef": {
                            "Value": "2021-02-03"
                        },
                        "DatedVehicleJourneyRef": "646903"
                        },
                        "JourneyPatternRef": {
                        "Value": "27"
                        },
                        "LineRef": {
                        "Value": "174"
                        },
                        "Monitored": True,
                        "MonitoredCall": {
                        "StopPointName": [
                            {
                            "Value": "X1 King William St"
                            }
                        ],
                        "StopPointRef": {
                            "Value": "16281"
                        },
                        "AimedArrivalTime": "/Date(1612350540000+1030)/",
                        "AimedArrivalTimeSpecified": True,
                        "AimedDepartureTime": "/Date(0)/",
                        "AimedLatestPassengerAccessTime": "/Date(0)/",
                        "DestinationDisplay": {
                            "Value": "Paradise"
                        },
                        "EarliestExpectedDepartureTime": "/Date(0)/",
                        "ExpectedLatestPassengerAccessTime": "/Date(0)/",
                        "Item": "/Date(0)/",
                        "Item1": "/Date(0)/",
                        "LatestExpectedArrivalTime": "/Date(1612350557000+1030)/",
                        "LatestExpectedArrivalTimeSpecified": True,
                        "ProvisionalExpectedDepartureTime": "/Date(0)/",
                        "VehicleLocationAtStop": {
                            "Items": ["-34.923921", "138.599433"]

                        }
                        },
                        "MonitoredSpecified": True,
                        "OperatorRef": {
                        "Value": "5 - Adelaide Metro (Torrens Transit)"
                        },
                        "OriginAimedDepartureTime": "/Date(0)/",
                        "VehicleLocation": {
                        "Items": ["-34.9710", "138.6185"]
                        },
                        "VehicleRef": {
                        "Value": "1932"
                        }
                    },
                    "MonitoringRef": {
                        "Value": "16281"
                    },
                    "StopVisitNote": [
                        {
                        "Value": "StopType=BS"
                        }
                    ],
                    "ValidUntilTime": "/Date(0)/"
                    }
                ],
                "MonitoringRef": [
                    {
                    "Value": "16281"
                    }
                ],
                "version": "2.0"
                }
            ]
            }

    def __init__(self, stop_code):

        self.next_services = list()
        self.stop_code = stop_code
        self.real_time_data = self._check_real_time()
        self._build_next_services()


    def _check_real_time(self):
        try:
            r = requests.get(f"{self.REAL_TIME_API}{self.stop_code}")
            data = r.json()
            #data = self.test_data
            
            return data
        except Exception as e:
            print(e)

    def _arrives_in(self, arrival_time: datetime):
        now = datetime.now()
        # now = datetime(2021,2,3,21,21,0) # for test data
        at = arrival_time
        here_in = int((at - now).seconds/60)
        return f"{here_in} min" if here_in > 1 else "now"

    def track_bus(self, route:str):
        arr = [
        {
            "recorded_at": "2021-02-03T21:17:29",
            "journey_code": "3240",
            "destination_time": "2021-02-03T22:00:00",
            "destination": "Port Adelaide",
            "direction": "O",
            "trip_id": "648348",
            "route": "230",
            "stop_name": "X1 King William St",
            "stop_code": "16281",
            "aimed_time": "2021-02-03T21:21:00",
            "expected_time": "2021-02-03T21:21:57",
            "arrives_in": "86 min",
            "vehicle_location": [
            138.6062,
            -34.93194
            ]
        },
        {
            "recorded_at": "2021-02-03T21:13:54",
            "journey_code": "368",
            "destination_time": "2021-02-03T22:10:00",
            "destination": "Paradise",
            "direction": "O",
            "trip_id": "647113",
            "route": "178",
            "stop_name": "X1 King William St",
            "stop_code": "16281",
            "aimed_time": "2021-02-03T21:24:00",
            "expected_time": "2021-02-03T21:26:25",
            "arrives_in": "91 min",
            "vehicle_location": [
            138.6258,
            -34.95549
            ]
        },
        {
            "recorded_at": "2021-02-03T21:15:40",
            "journey_code": "3698",
            "destination_time": "2021-02-03T22:07:00",
            "destination": "Paradise",
            "direction": "O",
            "trip_id": "646903",
            "route": "174",
            "stop_name": "X1 King William St",
            "stop_code": "16281",
            "aimed_time": "2021-02-03T21:39:00",
            "expected_time": "2021-02-03T21:39:17",
            "arrives_in": "104 min",
            "vehicle_location": [
            138.6185,
            -34.971
            ]
        }
        ]

        arr = self.next_services

        sub = filter(lambda x : x["route"]==route , arr)
        return list(sub)
    
    def _build_next_services(self):

        next_services_response = self.real_time_data["StopMonitoringDelivery"][0].get("MonitoredStopVisit")
        if not next_services_response:
            return

        
        for next_service in next_services_response:
            ns_data = dict()
            recorded_time = str_to_date(next_service["RecordedAtTime"])
            destination_time = str_to_date(next_service["MonitoredVehicleJourney"]["DestinationAimedArrivalTime"])
            aimed_time = str_to_date(next_service["MonitoredVehicleJourney"]["MonitoredCall"]["AimedArrivalTime"])
            expected_time = str_to_date(next_service["MonitoredVehicleJourney"]["MonitoredCall"]["LatestExpectedArrivalTime"])
            ns_data["recorded_at"] = recorded_time
            ns_data["journey_code"] = next_service["MonitoredVehicleJourney"]["BlockRef"]["Value"]
            ns_data["destination_time"] = destination_time
            ns_data["destination"] = next_service["MonitoredVehicleJourney"]["DestinationName"][0]["Value"]
            ns_data["direction"] = next_service["MonitoredVehicleJourney"]["DirectionRef"]["Value"]
            ns_data["trip_id"] = next_service["MonitoredVehicleJourney"]["FramedVehicleJourneyRef"]["DatedVehicleJourneyRef"]
            ns_data["route"] = next_service["MonitoredVehicleJourney"]["LineRef"]["Value"]
            ns_data["stop_name"] = next_service["MonitoredVehicleJourney"]["MonitoredCall"]["StopPointName"][0]["Value"]
            ns_data["stop_code"] = next_service["MonitoredVehicleJourney"]["MonitoredCall"]["StopPointRef"]["Value"]
            ns_data["aimed_time"] = aimed_time
            ns_data["expected_time"] = expected_time
            ns_data["arrives_in"] = self._arrives_in(expected_time)
            ns_data["vehicle_location"] = [float(next_service["MonitoredVehicleJourney"]["VehicleLocation"]["Items"][1]),
                                            float(next_service["MonitoredVehicleJourney"]["VehicleLocation"]["Items"][0])]
            
            self.next_services.append(ns_data)
        
    