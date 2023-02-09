current_version = input().split('.')
current_version = ''.join(current_version)
current_version = int(current_version)
new_version = current_version + 1
new_version = str(new_version)
print('.'.join(new_version))
