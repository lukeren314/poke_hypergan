import subprocess

print("training model")
subprocess.call(
    ["hypergan train merged_data -s 128x128x3 -f png -c poke --resize -b 32 --device '/cpu:0' --save_every 500 --sample_every 5 --save_samples"], shell=True)
