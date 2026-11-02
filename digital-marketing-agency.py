agency_name = "Creative Digital"
team_size = 8
project_fee = 450000.0
is_accepting_clients = True

services = ["web design", "social media", "SEO", "branding"]
new_services = ["video editing", "AI automation"]

# Print all variables and data types
print(agency_name, type(agency_name))
print(team_size, type(team_size))
print(project_fee, type(project_fee))
print(is_accepting_clients, type(is_accepting_clients))
print(services, type(services))
print(new_services, type(new_services))

# if else checking
if project_fee >= 400000:
    print("High-value project")
else:
    print("Standard project")

# Print first, third and last services
print(services[0])
print(services[2])
print(services[-1])

# change SEO to SEO optimization
services[2] = "SEO optimization"

services.append("UX/UI Design")

services.insert(1, "content writing")

services.extend(new_services)

services.remove("branding")

services.pop()

del services[0]

print(services)