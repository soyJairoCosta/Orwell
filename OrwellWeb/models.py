from django.db import models
from django.utils import timezone

# Nodes that will conform the cluster
class Node(models.Model):
    # Name will be included in /etc/hosts as a new host
    name = models.CharField(max_length=10)
    # Ip will be included in /etc/host as a new host
    address_IP = models.CharField(max_length=15)
    mac_IP = models.CharField(max_length=17, blank=True, null=True)

    # Ip of the IPMI/BMC interface if exists
    address_IPMI = models.CharField(max_length=15, blank=True, null=True)
    mac_IPMI = models.CharField(max_length=17, blank=True, null=True)

    # Operative System of the node
    operative_system = models.CharField(max_length=20, blank=True, null=True)
    
    #HW INFORMATION START ====
    processor_name = models.CharField(max_length=17, blank=True, null=True)
    processor_number = models.IntegerField( 
        default=1,
        choices=((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),(7, '7'),(8, '8')),
        blank=True, 
        null=True)
    ram_info = models.CharField(max_length=20, blank=True, null=True)
    ram_number  = models.IntegerField(blank=True, null=True)
    gpu_info = models.CharField(max_length=20, blank=True, null=True)
    gpu_number  = models.IntegerField(blank=True, null=True)
    #HW INFORMATION END  ====

    # More information about the system
    description = models.TextField(blank=True, null=True)

    # Date of the node installation
    system_added  = models.DateTimeField(
            default=timezone.now)
    #Warranty of the node if exists
    warranty_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name