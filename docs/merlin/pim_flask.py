from flask import Flask, render_template_string
import psutil

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Physical Interface Monitor</title>
    <meta http-equiv="refresh" content="1"> <!-- auto-refresh every 1 sec -->
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 60%; }
        th, td { border: 1px solid #aaa; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .connected { color: green; font-weight: bold; }
        .disconnected { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h2>Physical Interface Monitor</h2>
    <table>
        <tr><th>Interface</th><th>Status</th></tr>
        {% for iface, connected in interfaces %}
        <tr>
            <td>{{ iface }}</td>
            <td class="{{ 'connected' if connected == 'Connected' else 'disconnected' }}">{{ connected }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

def get_interfaces():
    stats = psutil.net_if_stats()
    results = []

    for iface, stat in stats.items():
        # skip loopback and virtuals
        if iface.startswith(("lo", "docker", "veth", "br", "virbr", "vmnet")):
            continue

        connected = "Connected" if stat.isup else "Disconnected"
        results.append((iface, connected))

    return results

@app.route("/")
def index():
    interfaces = get_interfaces()
    return render_template_string(TEMPLATE, interfaces=interfaces)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
