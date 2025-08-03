---
title: "Vibe coding as a Software Engineer"
pubDate: 2025-06-27
author: Sumit Datta
categories: ['vibe coding', 'founder', 'software']
---

I started vibe coding early June 2025 with the aim to write as little code myself as possible. My intent is to be a founder with a lot of time for marketing, sales and support. I have been using LLM  assisted coding since late last year. I started with GitHub Copilot, then Codeium (now Windsurf) and settled on Supermaven for a while.

## Let's set some context:

1. I want to create fun, useful and error-free products, most of them small apps for consumers and businesses
2. Apps can be desktop, mobile, client-server - any combination, most of them will be open source and self-host friendly
3. Apps should integrate LLMs or other ML tools where deterministic code does not suffice
4. As a founder, I want to focus on users. Vibe coding should help me create products/features fast, very fast
5. I prefer to build products that face the user instead of API-first products

## Who is this for?

I am logging my thoughts and experiences for myself but these may be helpful if you:

1. Want to create software projects with minimal or no coding effort
2. Are open to spend some time setting up the best practices flow for vibe coding
3. Keep learning as vibe coding landscape changes

## Who is not not for?

You want to learn programming by doing (which is how I learnt myself). Programming is fun so keep doing that if you want. LLM assisted programming might be more useful for you.

## What does vibe coding mean?

I guess there are multiple definitions out there but vibe coding  generally means describing the software in simple human language and let LLM generate the code. This is different from LLM assisted coding where a software engineer is still using an editor to write the code with a pair-programmer (LLM).

Vibe coding is more like delegation. I have another (LLM) engineer who I can pass tasks to. They complete it, I check and move forward.

## The benefits

Without going into the debate about code quality yet, the main benefit for me is delegation. I have never been a delegation friendly person about code though. With LLMs it is a bit different, maybe it is psychological. I am happy to list out tasks and see the LLM work through them.

It has been saving me a lot of time. I am sure there are gaps in the software quality but I will be able to tighten them. At this moment, I do not have to be at desk all the time and I get multiple agents to work on multiple projects if I need.

## The process

I started off with Claude Code with API based usage. It was a joy to see some simple refactor produced only by describing what I thought should be improved in a couple modules.

Then I started a fresh project, a smart crawler. I wanted to create a desktop app that would control my browser, open URLs, crawl pages and get data as per a given objective. The objective is what I would have asked a team member to search some data on the web. I started off with having to specify the domains to crawl or fetch data from  (I would add web  search later).

I also started a travel planner app (full-stack) and a self-journal app (native app only, local storage).

I want to focus on the crawler for the rest of this post. I have written some crawlers before but I did not specify any in-depth programming logic, just a basic prompt:

> Please create a crawler and scraper in Rust. You can use any crates you want. The crawler will be given an objective and list of domains via command prompt. Objective may ask for existence of some information or list of extracted data or similar. The crawler should find the sitemap for any domain and ask Claude which URLs make most sense to crawl for the given objective. The crawler should be conservative in   crawling and try to use Claude to reach results fast.

This produced a working crawler with a CLI app. But it failed on sites which did not have a sitemap. So I share my second prompt:

> If a sitemap file is not found for a domain, can you generate a SiteMap from the links hierarchy found from the homepage or other pages? Then refer to this SiteMap as you continue crawling and base your decisions on it.

This did not work well, the way Claude wrote the code was to first crawl a bunch of URLs to generate a possible sitemap. It does not work, not sure why but it would also defeat the goal of a conservative crawl. To be honest, at this point I should have reverted the changes in this (second) prompt and restarted. Instead I started some of my technical thoughts in my prompts. I do not want to focus on them in this post since I want to focus on what is already good.

## The bad

At some point, in any project that grows in complexity, we will need our prompts to get more and more detailed, if not technical. But this is still something many builders/founders do not need to worry about for a large variety of small apps.


## The good

The first prompt could have been so much better but I was already surprised that everything worked as expected. No bugs. I did not ask for tests, which I should have. A prompt like that (may improved by Claude itself before putting into Claude Code) will be enough to describe many tiny app ideas for day to day software needs.

People need ad-hoc apps for a lot of personal or business use cases. In the last few weeks, I have used vibe coding daily, created 3-4 apps (backend, UI), created GitHub CI and release workflows (binaries and installers for all major OSes). Fixing errors was easy - just copy/paste and share with Claude Code.

The detail of HTML handling in the crawler when I asked for HTML cleaning or content finding improvements were just mind-blowing. Not because the code was very tough but because this is very laborious code with so many edge cases. LLMs have see tons of patterns in its learning corpus. What I am trying is basically codify them into an exhaustive HTML cleaner/parser so my LLM usage during crawling is low. This is a fascinating style of programming.

Overall, I am impressed and here are the reasons why:
- With a Claude Pro account, I am practically getting code for free
- With basic CI, generated code quality was good - ask Claude to write CI workflows for format checks, tests, etc.
- I learned about and started managing `Claude.md` - it helped setting the workflow
- Generated release workflow and it was easy to fix bugs happening on GitHub - just copy and paste
- Claude maintains my development workflow
- Test coverage is low, I suggest starting with TDD - again you do not need to understand the engineering side of this - just read best practices, setup `Claude.md` and it will give you huge returns
- Generated one page website, user facing README

The simple fact that I have a CLI app, website, CI/release workflows all working in a few days of vibe coding is worth many thousand of dollars.

## What to improve

The crawler is not a simple app and I knew this. It was a challenge to see how well vibe coding is and can I continue building a non-trivial product. I am very happy with how easily I can delegate work and get results. How smooth the (generated) workflow is. How low cost this is - Claude Pro account can be used with Claude Code. I am not even using Claude Max account!

I have freed up so much time to focus on marketing, share my journey (this post for example), while still moving the software development each day.
