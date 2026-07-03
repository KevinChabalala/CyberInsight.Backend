COMMON_PORTS = {

    20: {
        "service": "FTP Data",
        "risk": "High",
        "description": "FTP data transfer.",
        "recommendation": "Disable FTP and use SFTP."
    },

    21: {
        "service": "FTP",
        "risk": "Critical",
        "description": "FTP sends credentials in plaintext.",
        "recommendation": "Replace FTP with SFTP or FTPS."
    },

    22: {
        "service": "SSH",
        "risk": "Medium",
        "description": "Secure remote administration.",
        "recommendation": "Restrict SSH access using firewalls."
    },

    23: {
        "service": "Telnet",
        "risk": "Critical",
        "description": "Telnet is unencrypted.",
        "recommendation": "Disable Telnet."
    },

    25: {
        "service": "SMTP",
        "risk": "Medium",
        "description": "Mail Transfer Protocol.",
        "recommendation": "Configure SPF, DKIM and DMARC."
    },

    53: {
        "service": "DNS",
        "risk": "Low",
        "description": "Domain Name System.",
        "recommendation": "Disable open recursive DNS."
    },

    80: {
        "service": "HTTP",
        "risk": "Medium",
        "description": "Unencrypted web traffic.",
        "recommendation": "Redirect HTTP to HTTPS."
    },

    110: {
        "service": "POP3",
        "risk": "High",
        "description": "Mail retrieval protocol.",
        "recommendation": "Use POP3S or IMAPS."
    },

    143: {
        "service": "IMAP",
        "risk": "Medium",
        "description": "Email retrieval protocol.",
        "recommendation": "Use IMAPS."
    },

    443: {
        "service": "HTTPS",
        "risk": "Low",
        "description": "Encrypted web traffic.",
        "recommendation": "Maintain secure TLS configuration."
    },

    445: {
        "service": "SMB",
        "risk": "High",
        "description": "Windows file sharing.",
        "recommendation": "Restrict SMB exposure."
    },

    3306: {
        "service": "MySQL",
        "risk": "High",
        "description": "MySQL Database.",
        "recommendation": "Never expose MySQL publicly."
    },

    3389: {
        "service": "RDP",
        "risk": "Critical",
        "description": "Remote Desktop.",
        "recommendation": "Restrict RDP using VPN or firewall."
    },

    5432: {
        "service": "PostgreSQL",
        "risk": "High",
        "description": "PostgreSQL Database.",
        "recommendation": "Restrict external access."
    },

    6379: {
        "service": "Redis",
        "risk": "Critical",
        "description": "Redis Database.",
        "recommendation": "Require authentication and firewall rules."
    },

    8080: {
        "service": "HTTP Alternate",
        "risk": "Medium",
        "description": "Alternative web service.",
        "recommendation": "Verify exposure is intentional."
    },

    8443: {
        "service": "HTTPS Alternate",
        "risk": "Low",
        "description": "Alternative HTTPS service.",
        "recommendation": "Maintain secure TLS configuration."
    }

}