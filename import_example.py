from jpcli.main import jpcli
 
# Example for lsmem command
parsed_data = jpcli('lsmem', 'free')
print(parsed_data)

print("\n\n")

# Example for free command
parsed_data = jpcli('free -h')
print(parsed_data)

# Example for free command
#parsed_data = jpcli('lsblk')
#print(parsed_data)
