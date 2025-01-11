#!/bin/bash

# Function to collect system configuration features
collect_features() {
    ssh_root_login=$(grep -q "^PermitRootLogin yes" /etc/ssh/sshd_config && echo 1 || echo 0)
    firewall_active=$(ufw status | grep -q "active" && echo 1 || echo 0)
    permissions_secure=$(stat -c "%a" /etc/passwd | grep -q "644" && echo 1 || echo 0)
    system_up_to_date=$(apt list --upgradable 2>/dev/null | grep -q "upgradable" && echo 0 || echo 1)
    disk_usage_safe=$(df -h | awk '{if($5 > 90) print "0"}' | grep -q 0 && echo 0 || echo 1)

    # Return features as a comma-separated string
    echo "$ssh_root_login,$firewall_active,$permissions_secure,$system_up_to_date,$disk_usage_safe"
}

# Function to call the ML model (Python script)
predict_security() {
    features=$(collect_features)
    
    # Pass features to Python for prediction
    prediction=$(python3 predict_security.py "$features")

    # Based on prediction, provide recommendations
    if [ "$prediction" -eq 1 ]; then
        echo "The system is secure."
    else
        echo "The system is at risk. Recommendations:"
        echo "- Disable root login for SSH"
        echo "- Enable firewall"
        echo "- Secure file permissions"
        echo "- Run system updates"
        echo "- Check disk usage"
    fi
}

# Run the prediction
predict_security