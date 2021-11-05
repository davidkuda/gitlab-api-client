```bash
# get groups
'curl --header "PRIVATE-TOKEN: $TOKEN" \
    "https://gitlab.alexanderthamm.com/api/v4/groups"'

# get projects of a group
curl --header "PRIVATE-TOKEN: $TOKEN" \
    "https://gitlab.alexanderthamm.com/api/v4/groups/362/projects?per_page=50" \
    | jq -C '.[] | .name, .id'

# Show group vars
curl --header "PRIVATE-TOKEN: $TOKEN" \
"https://gitlab.alexanderthamm.com/api/v4/projects/473/variables"

# Create group vars
curl --request POST \
--header "PRIVATE-TOKEN: $TOKEN" \
"https://gitlab.alexanderthamm.com/api/v4/projects/473/variables" \
--form "key=DATA" --form "value=Dave 2021"
```