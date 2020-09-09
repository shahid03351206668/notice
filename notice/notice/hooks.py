# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "notice"
app_title = "Notice"
app_publisher = "Codes Soft"
app_description = "notice"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "shahid@codessoft.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/notice/css/notice.css"
# app_include_js = "/assets/notice/js/notice.js"

# include js, css files in header of web template
# web_include_css = "/assets/notice/css/notice.css"
# web_include_js = "/assets/notice/js/notice.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "notice.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "notice.install.before_install"
# after_install = "notice.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "notice.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Sales Order": {
        "before_cancel": "dcl.notice.check_reason"
    },
    "Sales Invoice": {
        "before_cancel": "dcl.notice.check_reason"
    },
    "Delivery Note": {
        "before_cancel": "dcl.notice.check_reason"
    },
    "Leave Application": {
        "before_cancel": "dcl.notice.check_reason"
    },
    "Purchase Order": {
        "before_cancel": "dcl.notice.check_reason"
    },
    "Purchase Receipt": {
        "before_cancel": "dcl.notice.check_reason"
    },
    "Purchase Invoice": {
        "before_cancel": "dcl.notice.check_reason"
    },
    "Material Request": {
        "before_cancel": "dcl.notice.check_reason"
    },
    "Stock Entry": {
        "before_cancel": "dcl.notice.check_reason"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"notice.tasks.all"
# 	],
# 	"daily": [
# 		"notice.tasks.daily"
# 	],
# 	"hourly": [
# 		"notice.tasks.hourly"
# 	],
# 	"weekly": [
# 		"notice.tasks.weekly"
# 	]
# 	"monthly": [
# 		"notice.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "notice.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "notice.event.get_events"
# }

