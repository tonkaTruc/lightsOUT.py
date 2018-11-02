import jsonpatch


def make_sender(uid, label):

    # Up to date with apiary mock server: 16/11/2017

    type = "multicast"
    status = True
    codec = "Calrec-32"                                         # Test variable
    packetTime = 125                                            # Test variable
    sampleRate = 96000                                          # Test variable
    originators = ["192.168.10.1 ", "192.168.10.2"]
    sourceAddresses = ["239.90.130.1 ", "239.90.130.1"]         # Test variable
    ports = [5004, 5006]                                        # Test variable
    sdpURIs = [
        "rtsp://192.168.10.1:8111/by-id/" + str(uid),
        "rtsp://192.168.10.1:8111/by-id/" + str(uid)
    ]
    channels = ["Aux1 - L", "Aux1 - R "]                        # Test variable
    sourcePorts = [0, 1, 2]                                     # Test variable

    # construct the patch with the above variables / <sender_value> is DICT format
    sender_value = {
        "sessionId": " ",
        "uid": uid,
        "type": type,
        "label": label,
        "status": status,
        "codec": codec,
        "packetTime": packetTime,
        "sampleRate": sampleRate,
        "originators": originators,
        "sourceAddresses": sourceAddresses,
        "ports": ports,
        "sdpURIs": sdpURIs,
        "channels": channels,
        "sourcePorts": sourcePorts
    }

    return sender_value


def make_receiver(uid, destPorts):

    # Up to date with apiary mock server: 16/11/2017

    label = "TEST_RECEIVER"
    type="multicast"
    linkOffset = 2000               # - Test variable
    nicMACs = (
        "e4:6f:13:f3:8e:b9",
        "e4:6f:13:f3:8e:b9"
    )
    codec = "calrec32"              # -
    status = True                   # -
    ports= [5004, 5006]
    sampleRate=96000

    # construct the patch with the above variables / <receiver_value> is DICT format
    receiver_value = {
        "uid": uid,                 # -
        "label": label,             # -
        "sampeTate": sampleRate,     # -
        "codec": codec,             # -
        "type": type,               # -
        "status": status,           # -
        "linkOffset": linkOffset,   # -
        "nicMACs": nicMACs,         # not in apiary
        "sessionId": " ",           # -
        "originators": [            # -
            " ",
            " "
        ],
        "destPorts": destPorts,     # -
        "destAddresses": [          # -
            " ",
            " "
        ],
        "ports": ports,             # -
        "channels":[                # -
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7
        ],
        "sdpURIs": [                # -
            " ",
            " "
        ]
    }

    return receiver_value


def make_add_patch(device_path, value):

    patch = jsonpatch.JsonPatch(
        [
            {
                "op": "add",
                "path": device_path,
                "value": value
            }
        ]
    )

    return patch


def make_remove_patch(path_to_remove):

    remove_patch = jsonpatch.JsonPatch(
        [
            {
                "op": "remove",
                "path": path_to_remove
            }
        ]
    )

    return remove_patch
