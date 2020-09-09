import frappe

def check_reason(self, method):
	if not self.reason_for_cancellation:
		frappe.throw("Reason for Cancellation is required.")