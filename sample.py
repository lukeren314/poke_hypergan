import subprocess

print("sampling model")
subprocess.call(
    ["hypergan sample merged_data -s 128x128x3 -f png -c poke --resize -b 32 --device '/cpu:0' --save_every 500 --sample_every 5 --save_samples"], shell=True)
