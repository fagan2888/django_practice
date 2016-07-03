from django.shortcuts import render

data = {
    1: {
        "name": "Huston Texans",
        "losses": 0,
        "power points": 38.78,
        "previous rank": 0,
        "wins": 1
    },
    2: {
        "name": "Quick as a coursing Rivers",
        "losses": 0,
        "power points": 26.36,
        "previous rank": 0,
        "wins": 1
    },
    3: {
        "name": "Cooper Scooper",
        "losses": 0,
        "power points": 25.7,
        "previous rank": 0,
        "wins": 1
    },
    4: {
        "name": "Cuban Raft Riders",
        "losses": 0,
        "power points": 20.44,
        "previous rank": 0,
        "wins": 1
    },
    5: {
        "name": "Stefon Diggs My Roster",
        "losses": 0,
        "power points": 18.4,
        "previous rank": 0,
        "wins": 1
    },
    6: {
        "name": "Moose Heights Mounties",
        "losses": 1,
        "power points": 17.11,
        "previous rank": 0,
        "wins": 0
    },
    7: {
        "name": "Aaron Out My Jackson",
        "losses": 1,
        "power points": 15.76,
        "previous rank": 0,
        "wins": 0
    },
    8: {
        "name": "Dennis The McManus",
        "losses": 0,
        "power points": 15.72,
        "previous rank": 0,
        "wins": 1
    },
    9: {
        "name": "The Hills Have Eyes",
        "losses": 1,
        "power points": 12.96,
        "previous rank": 0,
        "wins": 0
    },
    10: {
        "name": "The  Tannehilbillies",
        "losses": 1,
        "power points": 3.03,
        "previous rank": 0,
        "wins": 0
    },
    11: {
        "name": "Timbit Nation",
        "losses": 1,
        "power points": -2.01,
        "previous rank": 0,
        "wins": 0
    },
    12: {
        "name": "Richsaidchange Nameagain",
        "losses": 1,
        "power points": -2.38,
        "previous rank": 0,
        "wins": 0
    }
}

def index(request):
    return render(request, 'personal/home.html')

def rankings(request):
    return render(request, 'personal/rankings.html', {'data': sorted(data.items())})