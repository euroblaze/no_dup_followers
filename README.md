# Do Not Duplicate Followers on Record Duplication

This module prevents followers from being duplicated when duplicating Projects and Tasks in PwO v15.

## Installation

To install this module, simply copy it into your Odoo addons directory and update the module list in the Odoo Apps menu.

## Configuration

Use the Technical > System Parameters menu to set the `duplicate_followers` parameter:

- `1`: Followers will be duplicated when records are duplicated.
- `0`: Followers will not be duplicated.

By default, followers are not duplicated.

## Usage

After installation and configuration, the module will automatically apply the chosen behavior when duplicating Projects and Tasks.
