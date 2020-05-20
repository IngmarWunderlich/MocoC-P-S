"""List of API Enpoints the moco wrapper knows about."""

API_PATH = {
    "activity_get":                     "/activities/{id}",
    "activity_getlist":                 "/activities",
    "activity_create":                  "/activities",
    "activity_update":                  "/activities/{id}",
    "activity_delete":                  "/activities/{id}",
    "activity_start_timer":             "/activities/{id}/start_timer",
    "activity_stop_timer":              "/activities/{id}/stop_timer",
    "activity_disregard":               "/activities/disregard",
    "company_create":                   "/companies",
    "company_update":                   "/companies/{id}",
    "company_get":                      "/companies/{id}",
    "company_getlist":                  "/companies",
    "deal_create":                      "/deals",
    "deal_update":                      "/deals/{id}",
    "deal_get":                         "/deals/{id}",
    "deal_getlist":                     "/deals",
    "employment_get":                   "/users/employments/{id}",
    "employment_getlist":               "/users/employments",
    "holiday_getlist":                  "/users/holidays",
    "holiday_get":                      "/users/holidays/{id}",
    "holiday_create":                   "/users/holidays",
    "holiday_update":                   "/users/holidays/{id}",
    "holiday_delete":                   "/users/holidays/{id}",
    "invoice_getlist":                  "/invoices",
    "invoice_get":                      "/invoices/{id}",
    "invoice_locked":                   "/invoices/locked",
    "invoice_pdf":                      "/invoices/{id}.pdf",
    "invoice_timesheet":                "/invoices/{id}/timesheet.pdf",
    "invoice_update_status":            "/invoices/{id}/update_status",
    "invoice_create":                   "/invoices",
    "invoice_payment_getlist":          "/invoices/payments",
    "invoice_payment_get":              "/invoices/payments/{id}",
    "invoice_payment_create":           "/invoices/payments",
    "invoice_payment_update":           "/invoices/payments/{id}",
    "invoice_payment_delete":           "/invoices/payments/{id}",
    "invoice_payment_create_bulk":      "/invoices/payments/bulk",
    "offer_getlist":                    "/offers",
    "offer_get":                        "/offers/{id}",
    "offer_pdf":                        "/offers/{id}.pdf",
    "offer_create":                     "/offers",
    "presence_getlist":                 "/users/presences",
    "presence_get":                     "/users/presences/{id}",
    "presence_create":                  "/users/presences",
    "presence_update":                  "/users/presences/{id}",
    "presence_touch":                   "/users/presences/touch",
    "presence_delete":                  "/users/presences/{id}",
    "project_getlist":                  "/projects",
    "project_get":                      "/projects/{id}",
    "project_assigned":                 "/projects/assigned",
    "project_create":                   "/projects",
    "project_update":                   "/projects/{id}",
    "project_archive":                  "/projects/{id}/archive",
    "project_unarchive":                "/projects/{id}/unarchive",
    "project_report":                   "/projects/{id}/report",
    "project_contract_getlist":         "/projects/{project_id}/contracts",
    "project_contract_get":             "/projects/{project_id}/contracts/{contract_id}",
    "project_contract_create":          "/projects/{project_id}/contracts",
    "project_contract_update":          "/projects/{project_id}/contracts/{contract_id}",
    "project_contract_delete":          "/projects/{project_id}/contracts/{contract_id}",
    "project_expense_get":              "/projects/{project_id}/expenses/{expense_id}",
    "project_expense_getall":           "/projects/expenses",
    "project_expense_getlist":          "/projects/{project_id}/expenses",
    "project_expense_create":           "/projects/{project_id}/expenses",
    "project_expense_create_bulk":      "/projects/{project_id}/expenses/bulk",
    "project_expense_update":           "/projects/{project_id}/expenses/{expense_id}",
    "project_expense_delete":           "/projects/{project_id}/expenses/{expense_id}",
    "project_expense_disregard":        "/projects/{project_id}/expenses/disregard",
    "project_recurring_expense_getlist":"/projects/{project_id}/recurring_expenses",
    "project_recurring_expense_get":    "/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
    "project_recurring_expense_create": "/projects/{project_id}/recurring_expenses",
    "project_recurring_expense_delete": "/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
    "project_recurring_expense_update": "/projects/{project_id}/recurring_expenses/{recurring_expense_id}",
    "project_task_getlist":             "/projects/{project_id}/tasks",
    "project_task_get":                 "/projects/{project_id}/tasks/{task_id}",
    "project_task_create":              "/projects/{project_id}/tasks",
    "project_task_update":              "/projects/{project_id}/tasks/{task_id}",
    "project_task_delete":              "/projects/{project_id}/tasks/{task_id}",
    "contact_getlist":                  "/contacts/people",
    "contact_get":                      "/contacts/people/{id}",
    "contact_create":                   "/contacts/people",
    "contact_update":                   "/contacts/people/{id}",
    "comment_create":                   "/comments",
    "comment_update":                   "/comments/{id}",
    "comment_getlist":                  "/comments",
    "comment_get":                      "/comments/{id}",
    "comment_create_bulk":              "/comments/bulk",
    "comment_delete":                   "/comments/{id}",
    "unit_get":                         "/units/{id}",
    "unit_getlist":                     "/units",
    "user_get":                         "/users/{id}",
    "user_getlist":                     "/users",
    "user_create":                      "/users",
    "user_update":                      "/users/{id}",
    "user_delete":                      "/users/{id}",
    "schedule_get":                     "/schedules/{id}",
    "schedule_getlist":                 "/schedules",
    "schedule_create":                  "/schedules",
    "schedule_update":                  "/schedules/{id}",
    "schedule_delete":                  "/schedules/{id}",
    "deal_category_getlist":            "/deal_categories",
    "deal_category_get":                "/deal_categories/{id}",
    "deal_category_create":             "/deal_categories",
    "deal_category_update":             "/deal_categories/{id}",
    "deal_category_delete":             "/deal_categories/{id}",
    "session_auth":                     "/session",
    "project_payment_schedule_create":  "/projects/{project_id}/payment_schedules",
    "project_payment_schedule_getlist": "/projects/{project_id}/payment_schedules",
    "project_payment_schedule_get":     "/projects/{project_id}/payment_schedules/{schedule_id}",
    "project_payment_schedule_update":  "/projects/{project_id}/payment_schedules/{schedule_id}",
    "project_payment_schedule_delete":  "/projects/{project_id}/payment_schedules/{schedule_id}",
    "purchase_category_get":            "/purchases/categories/{id}",
    "purchase_category_getlist":        "/purchases/categories",
    "planning_entry_getlist":           "/planning_entries",
}
