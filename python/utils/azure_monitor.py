class AzureMonitor:
    def log_event(self, event_name, properties):
        print(f"AzureMonitor Event - {event_name}: {properties}")
