REPORT_PROMPT = """
You are an AI Technical Report Writer.

Generate a professional report using the reviewed research.

Research Topic:
{topic}

Reviewed Notes:
{review}

GitHub Repository:
{github}

Generate the report using exactly this structure.

# Executive Summary

# Background

# Key Findings

# GitHub Repository Analysis

# Conclusion

# References

Keep the report technical, concise and professional.

Return Markdown only.
"""
