await query.edit_message_text(instructions, parse_mode=ParseMode.MARKDOWN)
                
            elif data == "show_help":
                help_text = """❓ **HELP - Enhanced Proxy Checker Bot**

🏠 **RESIDENTIAL CHECKER:**
- 🔍 Deep analysis of proxy quality
- 📡 ISP detection and scoring
- 📱 Mobile/hosting identification
- ⭐ Premium threshold: 35+ points
- 🐌 Slower but more detailed
- 🎯 Best for: Quality over quantity

⚡ **FAST CHECKER:**
- 🚀 Quick HTTP connectivity test
- ✅ Basic working validation
- ⏱️ Response time measurement
- ❌ No quality analysis
- 🏃‍♂️ Faster processing
- 🎯 Best for: Quantity over quality

🌐 **GOOGLE CHECKER:**
- 🔍 Tests Google.com accessibility
- 🛡️ Detects blocking/CAPTCHA
- 📊 Verifies response content
- 🎯 Google-specific testing
- 🌐 Best for: Google access verification

📋 **SUPPORTED FORMATS:**
• `ip:port`
• `ip:port:user:pass`
• `user:pass@ip:port`
• `http://ip:port`
• `socks5://ip:port`

📊 **LIMITS & SPECS:**
• 📈 Max proxies: 100,000
• 💾 Max file size: 16MB
• 📄 File format: .txt only

💻 **COMMANDS:**
• `/start` - Main menu
• `/cancel` - Stop active session

🚀 **NEW FEATURES:**
• Google Colab optimized
• Memory management
• Keep-alive system
• Enhanced performance

Choose mode based on your needs!"""
                
                keyboard = [
                    [InlineKeyboardButton("🔙 Back to Menu", callback_data="back_to_menu")]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                await query.edit_message_text(help_text, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)
                
            elif data == "back_to_menu":
                welcome_text = """🤖 Enhanced Proxy Checker Bot

🎯 Choose your checking mode:

🏠 **RESIDENTIAL CHECKER:**
- 🏛️ Premium residential proxy detection
- 📊 Advanced IP analysis and scoring
- ⭐ Quality score: 35+ points
- ⚙️ Settings: 6s timeout, 75 concurrent
- 🎯 Best for: Finding high-quality residential proxies

⚡ **FAST CHECKER:**
- 🚀 Ultra-fast HTTP connectivity testing
- ✅ Basic working proxy detection
- ⚙️ Settings: 4s timeout, 150 concurrent
- 🎯 Best for: Quick proxy validation

🌐 **GOOGLE CHECKER:**
- 🔍 Tests proxy access to Google.com
- 🌐 Verifies Google accessibility without blocks
- ⚙️ Settings: 8s timeout, 50 concurrent
- 🎯 Best for: Google-specific proxy testing

📈 **NEW LIMITS:** 100,000 proxies for all modes!
🔧 **Enhanced:** Google Colab optimized, memory managed

Select your preferred mode below:"""
                
                keyboard = [
                    [InlineKeyboardButton("🏠 Residential Checker", callback_data="mode_residential")],
                    [InlineKeyboardButton("⚡ Fast Checker", callback_data="mode_fast")],
                    [InlineKeyboardButton("🌐 Google Checker", callback_data="mode_google")],
                    [InlineKeyboardButton("❓ Help", callback_data="show_help")]
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)
                
                await query.edit_message_text(welcome_text, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)
                
            elif data == "cancel_session":
                if user_id not in self.active_sessions:
                    await query.edit_message_text("❌ No active session found.")
                    return
                
                self.active_sessions[user_id]['is_cancelled'] = True
                await query.edit_message_text("🛑 Session cancelled successfully.\n\n🔄 Use /start to restart.")
                
                await asyncio.sleep(2)
                if user_id in self.active_sessions:
                    del self.active_sessions[user_id]
                    gc.collect()
                    
        except Exception as e:
            logger.error(f"Button error: {e}")
            try:
        print("="*70)
        print("🤖 ENHANCED PROXY CHECKER BOT FOR GOOGLE COLAB")
        print("="*70)
        print(f"🔑 Token: {BOT_TOKEN[:10]}...{BOT_TOKEN[-10:]}")
        print(f"👤 Admin IDs: {ADMIN_IDS}")
        print(f"🎯 Features: Enhanced Residential + Ultra-Fast + Google modes")
        print(f"🏠 Residential: Premium detection, quality scoring")
        print(f"⚡ Fast: Ultra-fast HTTP connectivity testing")
        print(f"🌐 Google: Google.com accessibility testing")
        print(f"📊 Limits: 100,000 proxies per mode")
        print(f"🚀 Enhanced: Google Colab optimized, keep-alive, memory managed")
        print("="*70)
        
        # Setup environment
        setup_colab_environment()
        
        # Test connection
        print("🔍 Testing connection...")
        if test_bot_connection():
            print("✅ CONNECTION SUCCESSFUL!")
            print("🤖 Your enhanced bot is ready to run!")
            print("📱 Features enabled:")
            print("  • 🔧 Google Colab keep-alive system")
            print("  • 💾 Memory monitoring and optimization")
            print("  • 📈 100K proxy limit")
            print("  • 🚀 Enhanced performance settings")
            print("  • 🛡️ Advanced error handling")
            print("  • 📊 Real-time progress tracking")
            print("  • 🌐 NEW: Google Checker mode")
            print("\n🔄 Next step: Run 'await run_bot()' to start the enhanced bot")
        else:
            print("❌ CONNECTION FAILED!")
            print("🔧 Please check:")
            print("1. 🤖 Bot token is correct")
            print("2. 🌐 Internet connection is working") 
            print("3. 🛡️ Bot is not blocked by @BotFather")
            print("4. 📦 All required packages are installed")
        
        print("="*70)
            
    except Exception as e:
        logger.error(f"Main function error: {e}")
        print(f"❌ Error in main: {e}")
        traceback.print_exc()


# Auto-run setup when imported
if __name__ == "__main__":
    main()

# For Google Colab users - uncomment the line below to auto-start the bot
# asyncio.create_task(run_bot())

print("\n" + "="*70)
print("🚀 ENHANCED PROXY CHECKER BOT READY!")
print("="*70)
print("🔄 To start the bot, run:")
print("await run_bot()")
print("")
print("🎯 Features:")
print("• 🔧 Google Colab keep-alive (prevents disconnection)")
print("• 💾 Memory monitoring and auto-cleanup")
print("• 📈 100,000 proxy limit per mode")
print("• 🚀 Enhanced performance (50-150 concurrent)")
print("• 🏠 Advanced residential detection")
print("• ⚡ Ultra-fast basic checking")
print("• 🌐 NEW: Google accessibility testing")
print("• 📊 Real-time progress tracking")
print("• 🛡️ Robust error handling")
print("="*70)
                await query.edit_message_text("❌ Error occurred. Please try /start again.")
            except:
                pass


async def run_bot():
    """Run the bot with enhanced error handling and keep-alive features"""
    
    print("🔍 Testing bot connection first...")
    if not test_bot_connection():
        print("❌ Bot connection failed! Check your token.")
        return
    
    try:
        print("🔧 Creating enhanced bot application...")
        
        # Create application with enhanced settings for 100k proxies
        application = (
            Application.builder()
            .token(BOT_TOKEN)
            .read_timeout(60)  # Increased timeouts for large operations
            .write_timeout(60)
            .connect_timeout(60)
            .pool_timeout(60)
            .concurrent_updates(256)  # Handle more concurrent updates
            .build()
        )
        
        bot_instance = CombinedProxyBot()
        print("✅ Enhanced bot instance created with background systems")
        
        # Add handlers
        application.add_handler(CommandHandler("start", bot_instance.start))
        application.add_handler(CommandHandler("cancel", bot_instance.cancel_command))
        
        # Admin commands
        application.add_handler(CommandHandler("stats", bot_instance.admin_stats))
        application.add_handler(CommandHandler("broadcast", bot_instance.admin_broadcast))
        application.add_handler(CommandHandler("cancelall", bot_instance.admin_cancel_all))
        application.add_handler(CommandHandler("userinfo", bot_instance.admin_user_info))
        application.add_handler(CommandHandler("admins", bot_instance.admin_help))
        
        application.add_handler(MessageHandler(filters.Document.ALL, bot_instance.handle_document))
        application.add_handler(CallbackQueryHandler(bot_instance.button_handler))
        
        # Enhanced error handler
        async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
            logger.error(f"Bot error: {context.error}")
            if update and update.effective_user:
                try:
                    await context.bot.send_message(
                        update.effective_user.id,
                        "❌ An error occurred. Please try /start again.\n\n🔧 If issues persist, the bot may be processing a large dataset."
                    )
                except Exception as send_error:
                    logger.error(f"Failed to send error message: {send_error}")
        
        application.add_error_handler(error_handler)
        print("✅ All handlers registered")
        
        # Display enhanced info
        print("\n" + "="*70)
        print("🤖 ENHANCED PROXY CHECKER BOT - GOOGLE COLAB OPTIMIZED")
        print("="*70)
        print(f"🔑 Token: {BOT_TOKEN[:10]}...{BOT_TOKEN[-10:]}")
        print(f"👤 Admin: {ADMIN_IDS[0]}")
        print(f"🎯 Modes: Enhanced Residential + Ultra-Fast + Google Checker")
        print(f"🏠 Residential: 6s timeout, 75 concurrent, 100k max")
        print(f"⚡ Fast: 4s timeout, 150 concurrent, 100k max")
        print(f"🌐 Google: 8s timeout, 50 concurrent, 100k max")
        print(f"🚀 Features: Keep-alive, Memory management, Auto-cleanup")
        print(f"👨‍💻 Admin Commands: /stats, /broadcast, /cancelall, /userinfo, /admins")
        print("="*70)
        print("🔄 BOT IS STARTING WITH ENHANCED FEATURES...")
        print("📱 Go to Telegram and find your bot!")
        print("🔧 Google Colab will stay alive automatically!")
        print("="*70)
        
        # Initialize with enhanced settings
        await application.initialize()
        await application.start()
        
        # Start enhanced polling
        print("🔍 Starting enhanced polling...")
        
        await application.updater.start_polling(
            allowed_updates=Update.ALL_TYPES,
            drop_pending_updates=True,
            read_timeout=60,
            write_timeout=60,
            connect_timeout=60,
            pool_timeout=60
        )
        
        print("✅ BOT IS NOW ONLINE WITH ENHANCED FEATURES!")
        print("📱 Open Telegram and send /start to your bot")
        print("🌐 Google Checker mode is now available!")
        print("🔄 Keep-alive system is active - Colab won't disconnect!")
        print("💾 Memory monitoring is active")
        print("📈 100K proxy limit enabled for all modes")
        print("🤖 Bot is running... (Interrupt to stop)")
        
        # Enhanced keep-alive loop
        consecutive_errors = 0
        max_consecutive_errors = 5
        
        try:
            while True:
                await asyncio.sleep(10)  # Check every 10 seconds
                
                # Enhanced health check
                try:
                    me = await application.bot.get_me()
                    if not me:
                        print("❌ Bot connection lost, attempting reconnection...")
                        consecutive_errors += 1
                        if consecutive_errors >= max_consecutive_errors:
                            print("🔴 Too many consecutive errors, restarting...")
                            break
                    else:
                        consecutive_errors = 0  # Reset error counter
                        
                    # Memory check and cleanup
                    memory = psutil.virtual_memory()
                    if memory.percent > 85:
                        print(f"🔴 High memory usage: {memory.percent:.1f}% - Forcing cleanup")
                        gc.collect()
                        
                        # Cancel old sessions if memory is still high
                        if memory.percent > 90:
                            print("🚨 Emergency memory cleanup - cancelling old sessions")
                            for session in list(bot_instance.active_sessions.values()):
                                if time.time() - session.get('start_time', 0) > 3600:  # 1 hour old
                                    session['is_cancelled'] = True
                    
                    # Periodic status report
                    current_time = time.time()
                    if hasattr(run_bot, 'last_status_time'):
                        if current_time - run_bot.last_status_time > 1800:  # Every 30 minutes
                            active_sessions = len(bot_instance.active_sessions)
                            print(f"📊 Status: {active_sessions} active sessions, {memory.percent:.1f}% memory")
                            run_bot.last_status_time = current_time
                    else:
                        run_bot.last_status_time = current_time
                        
                except Exception as health_error:
                    consecutive_errors += 1
                    print(f"⚠️ Health check failed ({consecutive_errors}/{max_consecutive_errors}): {health_error}")
                    
                    if consecutive_errors >= max_consecutive_errors:
                        print("🔴 Health check failed too many times, attempting restart...")
                        break
                    
                    await asyncio.sleep(30)  # Wait longer after error
                    
        except KeyboardInterrupt:
            print("\n🛑 Bot stopped by user")
        except Exception as run_error:
            print(f"\n❌ Runtime error: {run_error}")
            traceback.print_exc()
        
    except Exception as e:
        print(f"\n❌ Failed to start: {e}")
        traceback.print_exc()
        print("\n🔧 TRY THESE FIXES:")
        print("1. 🔄 Restart Colab runtime")
        print("2. 🌐 Check internet connection")
        print("3. 🤖 Verify bot token with @BotFather")
        print("4. 📦 Install required packages: !pip install python-telegram-bot aiohttp psutil")
        
    finally:
        try:
            print("🔄 Shutting down gracefully...")
            if 'application' in locals():
                # Cancel all active sessions
                if 'bot_instance' in locals():
                    for session in bot_instance.active_sessions.values():
                        session['is_cancelled'] = True
                
                await application.stop()
                await application.shutdown()
                gc.collect()
            print("✅ Shutdown complete")
        except Exception as shutdown_error:
            print(f"⚠️ Shutdown error: {shutdown_error}")


def setup_colab_environment():
    """Setup the Google Colab environment for optimal performance"""
    print("🔧 Setting up Google Colab environment...")
    
    try:
        # Install required packages if not present
        import subprocess
        import sys
        
        required_packages = [
            'python-telegram-bot>=20.0',
            'aiohttp>=3.8.0',
            'psutil>=5.9.0',
            'nest-asyncio>=1.5.0'
        ]
        
        for package in required_packages:
            try:
                __import__(package.split('>=')[0].replace('-', '_'))
            except ImportError:
                print(f"📦 Installing {package}...")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        
        print("✅ All required packages are installed")
        
        # Configure Colab settings
        os.environ['COLAB_OPTIMIZE'] = '1'
        
        print("✅ Google Colab environment configured")
        return True
        
    except Exception as e:
        print(f"⚠️ Environment setup warning: {e}")
        return False


def main():
    """Main function with enhanced Google Colab support"""
    try:    async def handle_document(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle uploaded proxy file"""
        try:
            user_id = update.effective_user.id
            
            if not context.user_data.get('waiting_for_file'):
                await update.message.reply_text("❌ Use /start command first and select a mode!")
                return
            
            document = update.message.document
            
            # Validate file
            if not document.file_name.endswith('.txt'):
                await update.message.reply_text("❌ Send a .txt file only!")
                return
            
            if document.file_size > 16 * 1024 * 1024:  # 16MB limit for 100k proxies
                await update.message.reply_text("❌ File too large! Max: 16MB")
                return
            
            processing_msg = await update.message.reply_text("⏳ Processing file...")
            
            try:
                # Download file
                file = await context.bot.get_file(document.file_id)
                file_content = await file.download_as_bytearray()
                
                # Decode content
                try:
                    content = file_content.decode('utf-8')
                except UnicodeDecodeError:
                    try:
                        content = file_content.decode('latin-1')
                    except UnicodeDecodeError:
                        content = file_content.decode('utf-8', errors='ignore')
                
                lines = content.splitlines()
                
                # Clean proxies
                raw_proxies = []
                for line in lines:
                    clean_line = line.strip()
                    if clean_line and not clean_line.startswith('#'):
                        raw_proxies.append(clean_line)
                
                if not raw_proxies:
                    await processing_msg.edit_text("❌ No valid proxies found!")
                    return
                
                max_proxies = 100000  # Increased limit to 100k
                if len(raw_proxies) > max_proxies:
                    await processing_msg.edit_text(
                        f"❌ Too many proxies! Found: {len(raw_proxies):,}, Max: {max_proxies:,}"
                    )
                    return
                
                await processing_msg.delete()
                context.user_data['waiting_for_file'] = False
                await self.start_checking(update, context, raw_proxies, document.file_name)
                
            except Exception as file_error:
                logger.error(f"File error: {file_error}")
                await processing_msg.edit_text(f"❌ File processing error: {str(file_error)[:50]}")
                
        except Exception as e:
            logger.error(f"Document handler error: {e}")
            await update.message.reply_text("❌ File processing failed. Try again.")

    async def start_checking(self, update: Update, context: ContextTypes.DEFAULT_TYPE, proxies, filename):
        """Start the checking process"""
        try:
            user_id = update.effective_user.id
            mode = context.user_data.get('mode')
            
            # Update user stats with mode preference
            self.update_user_stats(user_id, update.effective_user.username or 'None', 
                                 update.effective_user.first_name or 'Unknown', mode)
            
            if user_id in self.active_sessions:
                await update.message.reply_text("❌ Session already exists!")
                return
            
            print(f"🔄 Starting {mode} check for user {user_id}: {len(proxies):,} proxies")
            
            # Create session based on mode
            if mode == 'residential':
                session = {
                    'user_id': user_id,
                    'proxies': proxies,
                    'filename': filename,
                    'mode': mode,
                    'start_time': time.time(),
                    'checked_count': 0,
                    'premium_proxies': [],
                    'total_proxies': len(proxies),
                    'is_cancelled': False,
                    'status_message_id': None
                }
                mode_text = "🏠 Premium Residential Detection"
                settings_text = "6s timeout, 75 concurrent"
                description = "This will analyze each proxy for quality and residential indicators!"
            elif mode == 'google':
                session = {
                    'user_id': user_id,
                    'proxies': proxies,
                    'filename': filename,
                    'mode': mode,
                    'start_time': time.time(),
                    'checked_count': 0,
                    'google_working_proxies': [],
                    'total_proxies': len(proxies),
                    'is_cancelled': False,
                    'status_message_id': None
                }
                mode_text = "🌐 Google Access Testing"
                settings_text = "8s timeout, 50 concurrent"
                description = "This will test each proxy for Google.com accessibility!"
            else:  # fast mode
                session = {
                    'user_id': user_id,
                    'proxies': proxies,
                    'filename': filename,
                    'mode': mode,
                    'start_time': time.time(),
                    'checked_count': 0,
                    'working_proxies': [],
                    'total_proxies': len(proxies),
                    'is_cancelled': False,
                    'status_message_id': None
                }
                mode_text = "⚡ Fast HTTP Checking"
                settings_text = "4s timeout, 150 concurrent"
                description = "This will test each proxy for basic HTTP connectivity!"
            
            self.active_sessions[user_id] = session
            
            # Initial status
            keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel_session")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            status_text = f"""🔄 Proxy Checking Started

📁 File: {filename}
📊 Proxies: {len(proxies):,}
🎯 Mode: {mode_text}
⚙️ Settings: {settings_text}
📋 Status: Initializing...

{description}"""
            
            message = await update.message.reply_text(status_text, reply_markup=reply_markup)
            session['status_message_id'] = message.message_id
            
            # Start checking
            asyncio.create_task(self.run_checking_process(context.bot, session))
            
        except Exception as e:
            logger.error(f"Start checking error: {e}")
            await update.message.reply_text("❌ Error starting. Try again.")

    async def run_checking_process(self, bot, session):
        """Main checking process with enhanced error handling"""
        try:
            print(f"🔄 Starting {session['mode']} process for user {session['user_id']}")
            
            # Choose checker based on mode
            if session['mode'] == 'residential':
                checker = EnhancedResidentialChecker(bot, session)
            elif session['mode'] == 'google':
                checker = GoogleProxyChecker(bot, session)
            else:
                checker = FastProxyChecker(bot, session)
            
            # Parse proxies
            print("📝 Parsing proxies...")
            parsed_proxies = []
            for line in session['proxies']:
                try:
                    parsed = checker.parse_proxy(line)
                    if parsed:
                        parsed_proxies.append(parsed)
                except Exception:
                    continue
            
            if not parsed_proxies:
                await self.send_error_message(bot, session, "No valid proxies found")
                return
            
            # Remove duplicates
            unique_proxies = list(dict.fromkeys(parsed_proxies))
            removed = len(parsed_proxies) - len(unique_proxies)
            if removed > 0:
                print(f"🔄 Removed {removed:,} duplicates")
            
            session['total_proxies'] = len(unique_proxies)
            print(f"✅ Ready to test {len(unique_proxies):,} unique proxies")
            
            # Run tests
            await checker.run_tests(unique_proxies)
            
            # Send results
            if not session.get('is_cancelled'):
                await self.send_final_results(bot, session)
            
        except Exception as e:
            logger.error(f"Process error: {e}")
            traceback.print_exc()
            await self.send_error_message(bot, session, str(e))
        
        finally:
            try:
                user_id = session['user_id']
                if user_id in self.active_sessions:
                    del self.active_sessions[user_id]
                gc.collect()  # Force cleanup
                print(f"✅ Finished and cleaned up for user {user_id}")
            except Exception:
                pass

    async def send_final_results(self, bot, session):
        """Send final results based on mode"""
        try:
            user_id = session['user_id']
            mode = session['mode']
            total_time = time.time() - session['start_time']
            
            if mode == 'residential':
                results = session.get('premium_proxies', [])
                result_type = "premium residential"
                emoji = "🏠"
                print(f"✅ Results: {len(results)} premium residential proxies found")
            elif mode == 'google':
                results = session.get('google_working_proxies', [])
                result_type = "Google-accessible"
                emoji = "🌐"
                print(f"✅ Results: {len(results)} Google-accessible proxies found")
            else:
                results = session.get('working_proxies', [])
                result_type = "working"
                emoji = "⚡"
                print(f"✅ Results: {len(results)} working proxies found")
            
            success_rate = (len(results) / session['total_proxies']) * 100 if session['total_proxies'] > 0 else 0
            avg_rate = session['total_proxies'] / total_time if total_time > 0 else 0
            
            summary = f"""🎉 Proxy Checking Complete!

{emoji} **Mode:** {mode.title()} Checker
📊 **Results:**
• Checked: {session['total_proxies']:,}
• {result_type.title()} found: {len(results):,}
• Success rate: {success_rate:.1f}%
• Time taken: {total_time:.1f}s
• Average rate: {avg_rate:.1f}/s

{f"🏆 Top {result_type} proxies:" if results else f"❌ No {result_type} proxies found"}"""
            
            if results:
                if mode == 'residential':
                    sorted_results = sorted(results, key=lambda x: x['details']['quality_score'], reverse=True)
                    for i, proxy_data in enumerate(sorted_results[:5], 1):
                        details = proxy_data['details']
                        summary += f"\n{i}. `{proxy_data['proxy']}`"
                        summary += f"\n   ⏱️ {proxy_data['response_time']}ms | ⭐ Score: {details['quality_score']} | 🌍 {details['country']}"
                elif mode == 'google':
                    sorted_results = sorted(results, key=lambda x: x.get('response_time', 9999))
                    for i, proxy_data in enumerate(sorted_results[:5], 1):
                        summary += f"\n{i}. `{proxy_data['proxy']}`"
                        summary += f"\n   ⏱️ {proxy_data['response_time']}ms | 📋 {proxy_data['status']}"
                else:
                    sorted_results = sorted(results, key=lambda x: x.get('response_time', 9999))
                    for i, proxy_data in enumerate(sorted_results[:5], 1):
                        summary += f"\n{i}. `{proxy_data['proxy']}`"
                        summary += f"\n   ⏱️ {proxy_data['response_time']}ms"
            
            await bot.send_message(user_id, summary, parse_mode=ParseMode.MARKDOWN)
            
            if results:
                await self.send_result_files(bot, user_id, session)
                
        except Exception as e:
            logger.error(f"Results error: {e}")

    async def send_result_files(self, bot, user_id, session):
        """Send result files based on mode"""
        try:
            mode = session['mode']
            
            if mode == 'residential':
                results = session.get('premium_proxies', [])
                file_prefix = "premium_residential"
                file_description = "🏠 Premium Residential Proxies"
                emoji = "🏠"
            elif mode == 'google':
                results = session.get('google_working_proxies', [])
                file_prefix = "google_accessible"
                file_description = "🌐 Google-Accessible Proxies"
                emoji = "🌐"
            else:
                results = session.get('working_proxies', [])
                file_prefix = "working_proxies"
                file_description = "⚡ Working Proxies"
                emoji = "⚡"
            
            if not results:
                return
                
            timestamp = int(time.time())
            
            # Clean file
            clean_content = ""
            for proxy_data in results:
                clean_content += f"{proxy_data['proxy']}\n"
            
            clean_file = io.BytesIO(clean_content.encode('utf-8'))
            clean_file.name = f"{file_prefix}_{timestamp}.txt"
            
            await bot.send_document(
                user_id,
                clean_file,
                caption=f"{file_description} ({len(results):,} found)"
            )
            
            # Detailed file
            detailed_content = f"# {file_description} Results\n"
            detailed_content += f"# Checked: {session['total_proxies']:,}\n"
            detailed_content += f"# Found: {len(results):,}\n"
            detailed_content += f"# Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            detailed_content += f"# Enhanced Bot - 100K Limit\n\n"
            
            if mode == 'residential':
                sorted_results = sorted(results, key=lambda x: x['details']['quality_score'], reverse=True)
                for proxy_data in sorted_results:
                    details = proxy_data['details']
                    detailed_content += f"{proxy_data['proxy']} # {proxy_data['response_time']}ms | Score: {details['quality_score']} | {details['country']} | {details['isp']} | IP: {details['ip']}\n"
            elif mode == 'google':
                sorted_results = sorted(results, key=lambda x: x.get('response_time', 9999))
                for proxy_data in sorted_results:
                    detailed_content += f"{proxy_data['proxy']} # {proxy_data['response_time']}ms | {proxy_data['status']}\n"
            else:
                sorted_results = sorted(results, key=lambda x: x.get('response_time', 9999))
                for proxy_data in sorted_results:
                    detailed_content += f"{proxy_data['proxy']} # {proxy_data['response_time']}ms | {proxy_data['ip']}\n"
            
            detailed_file = io.BytesIO(detailed_content.encode('utf-8'))
            detailed_file.name = f"detailed_{file_prefix}_{timestamp}.txt"
            
            await bot.send_document(
                user_id,
                detailed_file,
                caption=f"📋 Detailed Results with analysis"
            )
            
            print(f"📁 Files sent to user {user_id}")
            
        except Exception as e:
            logger.error(f"File sending error: {e}")

    async def send_error_message(self, bot, session, error):
        """Send error message"""
        try:
            user_id = session.get('user_id')
            if user_id:
                await bot.send_message(
                    user_id,
                    f"❌ **Error:** {str(error)[:150]}\n\n🔄 Try again with /start",
                    parse_mode=ParseMode.MARKDOWN
                )
        except Exception as e:
            logger.error(f"Error message failed: {e}")

    async def cancel_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Cancel session"""
        try:
            user_id = update.effective_user.id
            
            if user_id not in self.active_sessions:
                await update.message.reply_text("❌ No active session to cancel.")
                return
            
            self.active_sessions[user_id]['is_cancelled'] = True
            await update.message.reply_text("🛑 Session cancelled successfully.\n\n🔄 Use /start to begin again.")
            
            await asyncio.sleep(2)
            if user_id in self.active_sessions:
                del self.active_sessions[user_id]
                gc.collect()
                
        except Exception as e:
            logger.error(f"Cancel error: {e}")
            await update.message.reply_text("❌ Cancel failed.")

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle button clicks"""
        try:
            query = update.callback_query
            await query.answer()
            
            data = query.data
            user_id = update.effective_user.id
            
            if data == "mode_residential":
                context.user_data['mode'] = 'residential'
                context.user_data['waiting_for_file'] = True
                
                instructions = """📁 Send your proxy list file

🏠 **RESIDENTIAL CHECKER MODE SELECTED**

📋 **Supported formats:**
• `ip:port`
• `ip:port:username:password`  
• `username:password@ip:port`
• `http://ip:port`
• `socks5://ip:port`

📊 **Requirements:**
• 📄 .txt file format only
• 📝 One proxy per line
• 📈 Max 100,000 proxies
• 💾 Max file size: 16MB

🔍 **This mode will analyze each proxy for:**
- 📡 ISP type and residential indicators
- 🏠 Hosting/datacenter detection
- 📱 Mobile connection detection
- ⭐ Quality scoring (35+ = premium)

📤 Upload your file now..."""
                
                await query.edit_message_text(instructions, parse_mode=ParseMode.MARKDOWN)
                
            elif data == "mode_fast":
                context.user_data['mode'] = 'fast'
                context.user_data['waiting_for_file'] = True
                
                instructions = """📁 Send your proxy list file

⚡ **FAST CHECKER MODE SELECTED**

📋 **Supported formats:**
• `ip:port`
• `ip:port:username:password`  
• `username:password@ip:port`
• `http://ip:port`
• `socks5://ip:port`

📊 **Requirements:**
• 📄 .txt file format only
• 📝 One proxy per line
• 📈 Max 100,000 proxies
• 💾 Max file size: 16MB

🔍 **This mode will test for:**
- ✅ Basic HTTP connectivity
- ⏱️ Response time measurement
- 📊 IP extraction
- ⚡ Quick validation only

📤 Upload your file now..."""
                
                await query.edit_message_text(instructions, parse_mode=ParseMode.MARKDOWN)
                
            elif data == "mode_google":
                context.user_data['mode'] = 'google'
                context.user_data['waiting_for_file'] = True
                
                instructions = """📁 Send your proxy list file

🌐 **GOOGLE CHECKER MODE SELECTED**

📋 **Supported formats:**
• `ip:port`
• `ip:port:username:password`  
• `username:password@ip:port`
• `http://ip:port`
• `socks5://ip:port`

📊 **Requirements:**
• 📄 .txt file format only
• 📝 One proxy per line
• 📈 Max 100,000 proxies
• 💾 Max file size: 16MB

🔍 **This mode will test for:**
- 🌐 Google.com accessibility
- 🔍 Anti-bot detection bypass
- ⚠️ CAPTCHA/blocking detection
- 📊 Response verification

📤 Upload your file now..."""
                    import aiohttp
import asyncio
import time
import json
import random
from pathlib import Path
import threading
from urllib.parse import urlparse
import io
import tempfile
import os
from datetime import datetime
import logging
import traceback
import nest_asyncio
import requests
import gc
import psutil
import signal
from IPython.display import Javascript, display
import re

# Enable nested asyncio for Colab
nest_asyncio.apply()

# Telegram imports
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from telegram.constants import ParseMode

# Bot configuration
BOT_TOKEN = "8369356968:AAHzQJMnOWvor5w8FSOt6Ili5NvexWWg5Wo"
ADMIN_IDS = [6307224822]

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Keep-alive functions for Google Colab
def keep_colab_alive():
    """Prevent Colab from disconnecting by simulating user activity"""
    try:
        display(Javascript('''
        function KeepClicking(){
            console.log("Keeping Colab alive...");
            document.querySelector('#top-toolbar > colab-connect-button').click();
            setTimeout(KeepClicking, 60000); // Click every minute
        }
        setTimeout(KeepClicking, 60000);
        
        // Prevent tab from sleeping
        function preventSleep() {
            console.log("Preventing sleep...");
            document.querySelector('body').click();
        }
        setInterval(preventSleep, 30000); // Every 30 seconds
        
        // Keep connection alive
        function keepConnectionAlive() {
            fetch('/api/kernels', {method: 'GET'})
                .then(response => console.log('Connection kept alive'))
                .catch(error => console.log('Keep-alive failed:', error));
        }
        setInterval(keepConnectionAlive, 120000); // Every 2 minutes
        '''))
        print("✅ Colab keep-alive system activated!")
    except Exception as e:
        print(f"⚠️ Keep-alive setup failed: {e}")

def memory_monitor():
    """Monitor and manage memory usage"""
    def monitor_loop():
        while True:
            try:
                memory = psutil.virtual_memory()
                memory_percent = memory.percent
                
                if memory_percent > 80:
                    print(f"🔴 High memory usage: {memory_percent:.1f}%")
                    gc.collect()  # Force garbage collection
                elif memory_percent > 60:
                    print(f"🟡 Memory usage: {memory_percent:.1f}%")
                else:
                    print(f"🟢 Memory usage: {memory_percent:.1f}%")
                
                time.sleep(300)  # Check every 5 minutes
            except Exception as e:
                print(f"Memory monitor error: {e}")
                time.sleep(60)
    
    thread = threading.Thread(target=monitor_loop, daemon=True)
    thread.start()

def heartbeat_system():
    """Send periodic heartbeat to keep connection alive"""
    def heartbeat():
        while True:
            try:
                print(f"💓 Heartbeat: {datetime.now().strftime('%H:%M:%S')} - Bot running...")
                time.sleep(600)  # Every 10 minutes
            except Exception as e:
                print(f"Heartbeat error: {e}")
                time.sleep(60)
    
    thread = threading.Thread(target=heartbeat, daemon=True)
    thread.start()

# Test bot connection first
def test_bot_connection():
    """Test if bot token works"""
    try:
        print("Testing bot connection...")
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('ok'):
                bot_info = data.get('result', {})
                print(f"Bot connection successful!")
                print(f"Bot name: {bot_info.get('first_name', 'Unknown')}")
                print(f"Bot username: @{bot_info.get('username', 'Unknown')}")
                return True
            else:
                print(f"Bot API error: {data}")
                return False
        else:
            print(f"HTTP error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Connection test failed: {e}")
        return False


class GoogleProxyChecker:
    def __init__(self, bot, session):
        self.bot = bot
        self.session = session
        self.google_working_proxies = []
        self.checked_count = 0
        self.total_proxies = 0
        self.lock = threading.Lock()
        self.start_time = time.time()
        
        # Settings optimized for Google testing
        self.timeout = 8  # Longer timeout for Google
        self.max_concurrent = 50  # Moderate concurrency to avoid rate limiting
        self.chunk_size = 300  # Medium chunks for balanced performance
        
        # Multiple Google endpoints to test
        self.test_urls = [
            "https://www.google.com",
            "https://www.google.com/search?q=test",
            "https://www.google.com/robots.txt",
            "https://www.google.com/favicon.ico"
        ]
        
        # Real browser user agents
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        ]

    def parse_proxy(self, proxy_line):
        """Parse all different proxy formats"""
        proxy_line = proxy_line.strip()
        if not proxy_line or proxy_line.startswith('#'):
            return None
        
        # Remove (Http) prefix if present
        if proxy_line.startswith('(Http)'):
            proxy_line = proxy_line[6:]
        
        try:
            # Format: http://host:port
            if proxy_line.startswith(('http://', 'https://')):
                return proxy_line
            
            # Format: socks5://host:port (convert to http)
            if proxy_line.startswith('socks5://'):
                socks_part = proxy_line[9:]
                return f"http://{socks_part}"
            
            # Format: user:pass@host:port
            if '@' in proxy_line and proxy_line.count(':') >= 3:
                auth_part, host_port = proxy_line.split('@', 1)
                username, password = auth_part.split(':', 1)
                return f"http://{username}:{password}@{host_port}"
            
            # Format: IP:PORT:USERNAME:PASSWORD
            parts = proxy_line.split(':')
            if len(parts) >= 4:
                host, port, username = parts[0], parts[1], parts[2]
                password = ':'.join(parts[3:])
                return f"http://{username}:{password}@{host}:{port}"
            
            # Format: IP:PORT
            elif len(parts) == 2:
                host, port = parts[0], parts[1]
                return f"http://{host}:{port}"
        
        except Exception:
            pass
        
        return None

    def clean_proxy_output(self, proxy):
        """Clean proxy for output"""
        if proxy.startswith('http://'):
            return proxy[7:]
        elif proxy.startswith('https://'):
            return proxy[8:]
        return proxy

    def get_random_headers(self):
        """Generate realistic browser headers for Google"""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0'
        }

    async def test_google_access(self, session, proxy):
        """Test if proxy can access Google with comprehensive checks"""
        try:
            headers = self.get_random_headers()
            timeout_config = aiohttp.ClientTimeout(total=self.timeout, connect=self.timeout/2)
            
            # Test primary Google endpoint
            test_url = random.choice(self.test_urls)
            start_time = time.time()
            
            async with session.get(
                test_url,
                proxy=proxy,
                timeout=timeout_config,
                headers=headers,
                ssl=False,  # Allow unverified SSL for faster testing
                allow_redirects=True
            ) as response:
                
                end_time = time.time()
                response_time = round((end_time - start_time) * 1000, 2)
                
                # Check response status
                if response.status not in [200, 301, 302]:
                    return False, response_time, f"HTTP {response.status}", None
                
                # Get response content
                try:
                    content = await response.text()
                    content_lower = content.lower()
                    
                    # Verify it's actually Google
                    google_indicators = [
                        'google',
                        'search',
                        'gmail',
                        'gstatic',
                        'googletagmanager'
                    ]
                    
                    is_google = any(indicator in content_lower for indicator in google_indicators)
                    
                    if not is_google:
                        return False, response_time, "Not Google content", content[:100]
                    
                    # Check for blocking indicators
                    blocking_indicators = [
                        'captcha',
                        'blocked',
                        'unusual traffic',
                        'verify you are human',
                        'robot',
                        'automated queries'
                    ]
                    
                    is_blocked = any(indicator in content_lower for indicator in blocking_indicators)
                    
                    if is_blocked:
                        return False, response_time, "Google blocked/CAPTCHA", content[:100]
                    
                    # Success - can access Google normally
                    return True, response_time, "Google accessible", content[:100]
                    
                except Exception as content_error:
                    # If we can't read content but got 200, still consider it working
                    if response.status == 200:
                        return True, response_time, "Google accessible (no content)", None
                    return False, response_time, f"Content error: {str(content_error)[:30]}", None
                    
        except asyncio.TimeoutError:
            return False, 0, "Timeout", None
        except aiohttp.ClientProxyConnectionError:
            return False, 0, "Proxy connection failed", None
        except aiohttp.ClientConnectorError:
            return False, 0, "Connection failed", None
        except Exception as e:
            return False, 0, f"Error: {str(e)[:30]}", None

    async def test_proxy_comprehensive(self, session, proxy, semaphore):
        """Comprehensive proxy testing with Google access verification"""
        async with semaphore:
            try:
                # Test Google access
                is_working, response_time, status, content_sample = await self.test_google_access(session, proxy)
                
                result_data = {
                    'proxy': self.clean_proxy_output(proxy),
                    'response_time': response_time,
                    'status': status,
                    'is_working': is_working,
                    'content_sample': content_sample
                }
                
                return proxy, is_working, response_time, result_data, status
                    
            except Exception as e:
                return proxy, False, 0, None, f"Error: {str(e)[:30]}"

    async def test_proxies_chunk(self, proxies_chunk):
        """Test chunk of proxies for Google access"""
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        connector = aiohttp.TCPConnector(
            limit=self.max_concurrent * 2,
            ttl_dns_cache=300,
            use_dns_cache=True,
            keepalive_timeout=30,
            enable_cleanup_closed=True
        )
        
        timeout_config = aiohttp.ClientTimeout(total=self.timeout)
        
        async with aiohttp.ClientSession(
            connector=connector,
            timeout=timeout_config,
            skip_auto_headers=['User-Agent']
        ) as session:
            
            tasks = [self.test_proxy_comprehensive(session, proxy, semaphore) for proxy in proxies_chunk]
            
            for coro in asyncio.as_completed(tasks):
                if self.session.get('is_cancelled'):
                    break
                    
                try:
                    result = await coro
                    
                    with self.lock:
                        self.checked_count += 1
                        proxy, is_working, response_time, details, status = result
                        
                        if is_working and details:
                            proxy_data = {
                                'proxy': details['proxy'],
                                'response_time': response_time,
                                'status': status,
                                'details': details
                            }
                            self.google_working_proxies.append(proxy_data)
                            self.session['google_working_proxies'].append(proxy_data)
                            
                            print(f"✅ Google Access: {details['proxy']} | {response_time}ms | {status}")
                        
                        self.session['checked_count'] = self.checked_count
                        
                        # Progress update frequency
                        if self.checked_count % 25 == 0:
                            try:
                                await self.send_progress_update()
                                # Force garbage collection periodically
                                if self.checked_count % 500 == 0:
                                    gc.collect()
                            except Exception as e:
                                logger.error(f"Progress update error: {e}")
                                
                except Exception as task_error:
                    logger.error(f"Task error: {task_error}")
                    continue

    async def send_progress_update(self):
        """Send progress update to Telegram"""
        if self.session.get('is_cancelled'):
            return
        
        try:
            user_id = self.session['user_id']
            message_id = self.session.get('status_message_id')
            
            if not message_id:
                return
            
            elapsed = time.time() - self.start_time
            progress = (self.checked_count / self.total_proxies) * 100 if self.total_proxies > 0 else 0
            rate = self.checked_count / elapsed if elapsed > 0 else 0
            eta = (self.total_proxies - self.checked_count) / rate if rate > 0 else 0
            
            # Memory info
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            
            status_text = f"""🔍 Testing Google Access...

📊 Progress: {self.checked_count:,}/{self.total_proxies:,} ({progress:.1f}%)
⏰ Elapsed: {elapsed:.0f}s | Rate: {rate:.1f}/s
⏳ ETA: {eta:.0f}s remaining
🌐 Google Working: {len(self.google_working_proxies)}
💾 Memory: {memory_percent:.1f}%

🎯 Status: Testing Google.com accessibility..."""
            
            keyboard = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel_session")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await self.bot.edit_message_text(
                chat_id=user_id,
                message_id=message_id,
                text=status_text,
                reply_markup=reply_markup
            )
            
        except Exception as e:
            logger.error(f"Progress update error: {e}")

    async def run_tests(self, proxies):
        """Run all proxy tests for Google access"""
        self.total_proxies = len(proxies)
        self.session['total_proxies'] = self.total_proxies
        
        print(f"🔍 Testing {len(proxies):,} proxies for Google access...")
        
        chunks = [proxies[i:i + self.chunk_size] for i in range(0, len(proxies), self.chunk_size)]
        print(f"📦 Split into {len(chunks)} chunks of {self.chunk_size} proxies each")
        
        for i, chunk in enumerate(chunks):
            if self.session.get('is_cancelled'):
                break
            
            print(f"🔄 Processing chunk {i+1}/{len(chunks)} ({len(chunk)} proxies)...")
            
            try:
                await self.test_proxies_chunk(chunk)
            except Exception as chunk_error:
                logger.error(f"Chunk error: {chunk_error}")
                continue
            
            # Delay between chunks to avoid rate limiting
            if i < len(chunks) - 1:
                await asyncio.sleep(2)


class EnhancedResidentialChecker:
    def __init__(self, bot, session):
        self.bot = bot
        self.session = session
        self.premium_proxies = []
        self.checked_count = 0
        self.total_proxies = 0
        self.lock = threading.Lock()
        self.start_time = time.time()
        
        # Enhanced settings for 100k proxies
        self.timeout = 6  # Reduced timeout for faster processing
        self.max_concurrent = 75  # Increased concurrent connections
        self.test_url = "http://httpbin.org/ip"
        self.chunk_size = 200  # Increased chunk size
        
        # Real browser user agents
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
        ]

    def parse_proxy(self, proxy_line):
        """Parse all different proxy formats"""
        proxy_line = proxy_line.strip()
        if not proxy_line or proxy_line.startswith('#'):
            return None
        
        # Remove (Http) prefix if present
        if proxy_line.startswith('(Http)'):
            proxy_line = proxy_line[6:]
        
        try:
            # Format: http://host:port
            if proxy_line.startswith(('http://', 'https://')):
                return proxy_line
            
            # Format: socks5://host:port (convert to http)
            if proxy_line.startswith('socks5://'):
                socks_part = proxy_line[9:]
                return f"http://{socks_part}"
            
            # Format: user:pass@host:port
            if '@' in proxy_line and proxy_line.count(':') >= 3:
                auth_part, host_port = proxy_line.split('@', 1)
                username, password = auth_part.split(':', 1)
                return f"http://{username}:{password}@{host_port}"
            
            # Format: IP:PORT:USERNAME:PASSWORD
            parts = proxy_line.split(':')
            if len(parts) >= 4:
                host, port, username = parts[0], parts[1], parts[2]
                password = ':'.join(parts[3:])
                return f"http://{username}:{password}@{host}:{port}"
            
            # Format: IP:PORT
            elif len(parts) == 2:
                host, port = parts[0], parts[1]
                return f"http://{host}:{port}"
        
        except Exception:
            pass
        
        return None

    def clean_proxy_output(self, proxy):
        """Clean proxy for output"""
        if proxy.startswith('http://'):
            return proxy[7:]
        elif proxy.startswith('https://'):
            return proxy[8:]
        return proxy

    def get_random_headers(self):
        """Generate realistic browser headers"""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

    async def analyze_proxy_quality(self, session, proxy, ip_address):
        """Simplified IP analysis with reliable scoring"""
        quality_score = 0
        analysis_data = {}
        
        # Basic IP validation
        ip_parts = ip_address.split('.')
        if len(ip_parts) != 4:
            return 0, {}
        
        try:
            # Use IP-API for comprehensive analysis with reduced timeout for 100k processing
            url = f'http://ip-api.com/json/{ip_address}?fields=status,country,regionName,city,isp,org,as,proxy,hosting,mobile'
            async with session.get(url, proxy=proxy, timeout=aiohttp.ClientTimeout(total=8)) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    if data.get('status') == 'success':
                        analysis_data = data
                        
                        # Simplified scoring system
                        if not data.get('hosting', True):
                            quality_score += 30
                        
                        if not data.get('proxy', True):
                            quality_score += 30
                        
                        if data.get('mobile', False):
                            quality_score += 25
                        
                        # Check ISP for residential indicators
                        isp = data.get('isp', '').lower()
                        residential_keywords = [
                            'comcast', 'verizon', 'att', 'charter', 'cox', 'spectrum', 'xfinity',
                            'telecom', 'broadband', 'cable', 'fiber', 'dsl', 'residential'
                        ]
                        
                        datacenter_keywords = [
                            'amazon', 'google', 'microsoft', 'digitalocean', 'vultr', 'linode',
                            'ovh', 'hetzner', 'cloudflare', 'hosting', 'server', 'datacenter',
                            'cloud', 'vps', 'dedicated'
                        ]
                        
                        if any(keyword in isp for keyword in residential_keywords):
                            quality_score += 20
                        elif any(keyword in isp for keyword in datacenter_keywords):
                            quality_score -= 25
            
            await asyncio.sleep(0.3)  # Reduced rate limiting for speed
            
        except Exception as e:
            logger.debug(f"IP analysis failed for {ip_address}: {e}")
        
        return quality_score, analysis_data

    async def test_proxy_comprehensive(self, session, proxy, semaphore):
        """Comprehensive proxy testing with quality analysis"""
        async with semaphore:
            try:
                start_time = time.time()
                headers = self.get_random_headers()
                
                timeout_config = aiohttp.ClientTimeout(total=self.timeout, connect=self.timeout/2)
                
                async with session.get(
                    self.test_url,
                    proxy=proxy,
                    timeout=timeout_config,
                    headers=headers,
                    ssl=False
                ) as response:
                    
                    if response.status != 200:
                        return proxy, False, 0, None, "Failed connectivity"
                    
                    response_time = round((time.time() - start_time) * 1000, 2)
                    
                    # Extract IP
                    try:
                        data = await response.json()
                        ip_address = data.get('origin', '').split(',')[0].strip()
                    except:
                        ip_address = (await response.text()).strip()
                    
                    if not ip_address:
                        return proxy, False, 0, None, "No IP extracted"
                    
                    # Analyze proxy quality
                    quality_score, analysis_data = await self.analyze_proxy_quality(session, proxy, ip_address)
                    
                    # Speed bonus
                    if response_time > 2000:
                        quality_score += 10
                    elif response_time > 1000:
                        quality_score += 5
                    
                    # Determine if premium residential
                    is_premium = quality_score >= 35
                    
                    result_data = {
                        'ip': ip_address,
                        'response_time': response_time,
                        'quality_score': quality_score,
                        'country': analysis_data.get('country', 'Unknown'),
                        'isp': analysis_data.get('isp', 'Unknown'),
                        'is_hosting': analysis_data.get('hosting', True),
                        'is_proxy': analysis_data.get('proxy', True),
                        'is_mobile': analysis_data.get('mobile', False),
                        'is_premium': is_premium
                    }
                    
                    status = "PREMIUM RESIDENTIAL" if is_premium else f"NOT PREMIUM (Score: {quality_score})"
                    
                    return proxy, is_premium, response_time, result_data, status
                    
            except asyncio.TimeoutError:
                return proxy, False, 0, None, "Timeout"
            except Exception as e:
                return proxy, False, 0, None, f"Error: {str(e)[:30]}"

    async def test_proxies_chunk(self, proxies_chunk):
        """Test chunk of proxies with memory management"""
        semaphore = asyncio.Semaphore(self.max_concurrent)
        
        connector = aiohttp.TCPConnector(
            limit=self.max_concurrent * 2,
            ttl_dns_cache=300,
            use_dns_cache=True,
            keepalive_timeout=30,
            enable_cleanup_closed=True
        )
        
        timeout_config = aiohttp.ClientTimeout(total=self.timeout)
        
        async with aiohttp.ClientSession(
            connector=connector,
            timeout=timeout_config,
            skip_auto_headers=['User-Agent']
        ) as session:
            
            tasks = [self.test_proxy_comprehensive(session, proxy, semaphore) for proxy in proxies_chunk]
            
            for coro in asyncio.as_completed(tasks):
                if self.session.get('is_cancelled'):
                    break
                    
                try:
                    result = await coro
                    
                    with self.lock:
                        self.checked_count += 1
                        proxy, is_premium, response_time, details, status = result
                        
                        if is_premium and details:
                            clean_proxy = self.clean_proxy_output(proxy)
                            proxy_data = {
                                'proxy': clean_proxy,
                                'response_time': response_time,
                                'details': details
                            }
                            self.premium_proxies.append(proxy_data)
                            self.session['premium_proxies'].append(proxy_data)
                            
                            print(f"Premium: {clean_proxy} | {response_time}ms | Score: {details['quality_score']}")
                        
                        self.session['checked_count'] = self.checked_count
                        
                        # Reduced progress update frequency for performance
                        if self.checked_count % 50 == 0:
                            try:
                                await self.send_progress_update()
                                # Force garbage collection periodically
                                if self.checked_count % 1000 == 0:
                                    gc.collect()
                            except Exception as e:
                                logger.error(f"Progress update error: {e}")
                                
                except Exception as task_error:
                    logger.error(f"Task error: {task_error}")
                    continue

    async def send_progress_update(self):
        """Send progress update to Telegram"""
        if self.session.get('is_cancelled'):
            return
        
        try:
            user_id = self.session['user_id']
            message_id = self.session.get('status_message_id')
            
            if not message_id:
                return
            
            elapsed = time.time() - self.start_time
            progress = (self.checked_count / self.total_proxies) * 100 if self.total_proxies > 0 else 0
            rate = self.checked_count / elapsed if elapsed > 0 else 0
            eta = (self.total_proxies - self.checked_count) / rate if rate > 0 else 0
            
            # Memory info
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
