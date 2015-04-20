

cmd = '''curl -X POST -H "Content-Type: application/json" -d '{ "temperature": {"measurement": "20.22", "sensor_id": "1"}} ' https://temptor.herokuapp.com//temperatures.json'''
args=cmd.split()
process =subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr =process.communicate()
