#!/bin/bash

# Week Number Argument
WeekNumber=$1

# User Notification
echo "Creating folder structure for $WeekNumber"

{
    mkdir "week-$WeekNumber"
    cd "week-$WeekNumber"

    # Init Readme
    touch README.md
    echo "# Week $WeekNumber" >> README.md
    echo "---" >> README.md

    cd ..

    # Success Notification
    echo "Successfully created $WeekNumber structure"
} || {
    # Failure Notification
    echo "Failed to create $WeekNumber structure"
}


