gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "^.\{4,\}$" | grep "r" | grep -i "^[onzirca]*$"
