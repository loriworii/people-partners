---
name: cornerstone-course-recommender
description: >
  Recommend 3–5 Cornerstone LMS courses to an employee based on what they're
  trying to learn, achieve, or improve. Use this skill whenever someone asks
  for course recommendations, learning suggestions, or training ideas — whether
  they describe a job role ("I just became a people manager"), a skill gap
  ("I need to get better at data analysis"), a career goal ("I want to move
  into product"), or feedback they've received ("my manager said my
  communication needs work"). Also trigger when HR or L&D staff ask what
  courses to assign to a specific employee or team. Always use this skill
  rather than guessing — it fetches live data from the Cornerstone catalog.
---

# Cornerstone Course Recommender

You help employees find the right learning courses in Cornerstone based on
what they tell you about themselves — their role, the skills they want to build,
goals they're working toward, or feedback they've received.

## What you need to get started

You need these four things to connect to Cornerstone. If the user hasn't
provided them, ask before proceeding:

1. **Portal name** (`corpname`) — the subdomain of their Cornerstone portal,
   e.g. `acme` from `acme.csod.com`
2. **Client ID** — from Admin > Tools > Edge > API Management
3. **Client Secret** — generated when the OAuth app was registered
4. **Scope** — use `training:read` (or ask the user if they've configured a
   custom scope for catalog access)

If any of these are missing, ask for them directly. Don't guess.

---

## Step 1 — Understand what the employee needs

Before touching the API, read the prompt carefully. Figure out:

- **What they're trying to do or become.** A new manager? Sharpen Python
  skills? Prepare for a promotion? Improve based on feedback?
- **Key themes and topics** to search for. Pull out 2–4 distinct search terms
  from their description. Think broadly: if someone says "I want to become a
  better people manager," useful terms might be `management`, `leadership`,
  `coaching`, `feedback`.

If the prompt is vague (e.g. "recommend me some courses"), ask one clarifying
question: "What are you working on or trying to improve?"

---

## Step 2 — Authenticate with Cornerstone

Make a POST request to get an access token:

POST https://{corpname}.csod.com/services/api/oauth2/token
Content-Type: application/json

{
"clientId": "<client_id>",
"clientSecret": "<client_secret>",
"grantType": "client_credentials",
"scope": "training:read"
}


The response includes an `access_token`. Use it as a Bearer token in all
subsequent requests:

Authorization: Bearer <access_token>


Tokens expire after 3600 seconds (1 hour) by default. If you get a 401, the
token has likely expired — re-authenticate.

---

## Step 3 — Search the course catalog

Use the Cornerstone Catalog Search endpoint. Run one search per keyword/theme
you identified (you can run up to 4):

GET https://{corpname}.csod.com/services/api/x/content/v1/training?keyword={keyword}&lang=en-US&page=1&pageSize=20
Authorization: Bearer <access_token>


If the newer `x/content/v1` endpoint returns a 404, fall back to:

GET https://{corpname}.csod.com/services/api/Catalog/search?keyword={keyword}&lang=en-US
Authorization: Bearer <access_token>


From each response, collect the courses returned: their title, description,
training type (online course, video, curriculum, etc.), and any duration or
subject-area metadata that's available.

Deduplicate across searches — the same course may appear for multiple keywords.

---

## Step 4 — Select and present 3–5 courses

From all the results you collected, choose the 3–5 that are the best fit for
what the employee described. Prioritize:

- **Relevance** — does the course directly address what they said they need?
- **Coverage** — try to cover different angles of their need, not 5 courses on
  the exact same narrow topic
- **Type variety** — where possible, mix formats (e.g. a structured course plus
  a shorter video)

Present the recommendations like this:

---

### Recommended courses for [their name or "you"]

**1. [Course Title]** *(type, e.g. Online Course · 2 hrs)*
[One sentence explaining why this course fits their specific situation.]

**2. [Course Title]** *(type)*
[Reasoning.]

...and so on for 3–5 courses.

---

## Handling errors

| Error | What to do |
|-------|-----------|
| 401 Unauthorized | Token expired or wrong scope — re-authenticate or ask user to check scopes |
| 404 on endpoint | Try the fallback URL; if both fail, ask user to confirm their `corpname` |
| 429 Too Many Requests | Wait a few seconds and retry with exponential backoff |
| Empty results | Try broader keywords; tell the user what you searched for |

---

## Notes

- Always use Python (via bash) to make the API calls if direct HTTP isn't available. Use `requests` or `httpx`.
- Do not store or log the client secret beyond what's needed for this session.
- If the user asks to save credentials for future use, suggest they store them securely (e.g. a password manager or environment variable) rather than in a plain text file.
