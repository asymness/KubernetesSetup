pods=($(calicoctl get wep -o json | jq -r '.items[].spec.pod'))
interfaces=($(calicoctl get wep -o json | jq -r '.items[].spec.interfaceName'))
n=(${#pods[@]})

for i in $(seq 1 $n);
  do 
    interface=${interfaces[$i-1]}
    pod=${pods[$i-1]}
    tcpdump -i $interface -w ./caps/$pod.pcap &
done

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
        echo "** Stopping capture..."
	exit
}

read -r -d '' _ </dev/tty
