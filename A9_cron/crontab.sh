# 1. Set up a Daily File Cleanup Using Cron
0 2 * * * rm -rf /Users/justine/temp/*

# 2. Schedule a Weekly System Backup with Cron
0 3 * * 0 tar -czf /Users/justine/backups/backup_$(date +\%F).tar.gz /Users/justine/

# 4. Write command line for sending a Disk Usage Report using Cron
30 8 * * * df -h | mail -s "Disk Usage Report" legsonjm@example.com

