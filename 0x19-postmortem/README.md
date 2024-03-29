# Oops, We Tripped Up: The Great School Management System Outage of 2023 🚀

![Oops!](https://img.freepik.com/premium-vector/pop-art-style-with-oops-sign-banner-design-vector-illustration_194782-922.jpg?w=826)

**Issue Summary:**
- **Duration:** August 3, 2023, 08:45 AM - August 3, 2023, 11:30 AM (UTC-5)
- **Impact:** The school management system experienced a complete outage, affecting all users. Users encountered login errors, course material access issues, and assignment submission problems. Approximately 85% of users were affected.

**Timeline:**
- **Issue Detected:** August 3, 2023, 08:45 AM (UTC-5)
- **Detection Method:** Automated monitoring alert triggered due to unusually high server response time.
- **Actions Taken:** Initial investigation focused on backend servers and the database. Assumption: Database overload due to concurrent user activity.
- **Misleading Paths:** Temporary caching mechanism and network latency were explored as potential causes.
- **Escalation:** Incident was escalated to the DevOps and Database Management teams.
- **Resolution:** The issue was resolved by rolling back a recent database schema update that caused high CPU usage.

**Root Cause and Resolution:**
- **Root Cause:** The incident was caused by a poorly optimized database schema update, resulting in inefficient queries, elevated CPU load, and reduced response times.
- **Resolution:** The problematic database schema update was reverted to the previous version, mitigating the high CPU load and restoring normal system functioning. A comprehensive code review ensured similar issues were not present elsewhere.

*## **Corrective and Preventative Measures:**
- **Improvements/Fixes:**
  - Taught our database some yoga to optimize those queries.
  - Enlisted an AI bouncer for automated testing of database schema changes, so we can catch those party crashers.
  - Set up a hotline between the development and operations teams to prevent future surprises.
- **Tasks to Address Issue:**
  - Gave our database a makeover, ensuring it's always dressed to impress without the excess baggage.
  - Put our system on a treadmill with continuous monitoring for CPU usage, response times, and overall performance.
  - Decreed a strict dress code for code—no messy updates allowed without a thorough review.
  - Installed emergency exits with clear instructions for rollback in case our system decides to throw another tantrum.


This incident underscored the significance of robust testing and vigilant monitoring during system updates. The root cause analysis underscored the importance of optimized database queries and strong collaboration between development and operations teams.

Looking ahead, the proposed corrective and preventative measures will enhance the system's resilience and avert similar incidents. By embracing these changes, we aim to provide a dependable and seamless experience for all users of the school management system.
