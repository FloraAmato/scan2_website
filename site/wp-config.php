<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * Localized language
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wp_nlzri' );

/** Database username */
define( 'DB_USER', 'wp_hvl0j' );

/** Database password */
define( 'DB_PASSWORD', 'Aunp%^F%WxRo6s28' );

/** Database hostname */
define( 'DB_HOST', 'db' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY', 'VOmZesje1p#ly|n!Q]2Jg]9JOa6oB0AUG(38h/S-R#!6u2#O_po70|9%n@]Z)iM*');
define('SECURE_AUTH_KEY', '2u9*3uJ66J_1H*6cNZ9~#7NZHF|XR7AU(LT*M3g_FVwdl~G]45!p23%2ZQ72_%;;');
define('LOGGED_IN_KEY', '&0B3;AVZ3iKBM0Eh%07%8I0#S4Zeb2ub~)*;0|50l8!%53!!&dD!470r7+IuUtj~');
define('NONCE_KEY', 'RK6zTz4x(|3i78Dr/7P8ZnX7-a;eMwfs%eSC!T1yBa+06!;7r9chvsiW7q&Bb&j%');
define('AUTH_SALT', 'mm60[S)Zl[|6V190#n67(E#[y23A0)#_E~x*z&)l0JQ!bPmjJ0Z/4K&:u7fk82PV');
define('SECURE_AUTH_SALT', 'I-3-TMkG7OO-(~8KFTt;)wxO3d5!RoT7]WO6mF6/dM*_IH8vQcfH!3U8TS*sx8tB');
define('LOGGED_IN_SALT', 'N6B(%X-(+KF)cVKb])QSR+7VfBq90g02KtK|(6#7M8SL19KK&X2-S%;CB14xQuif');
define('NONCE_SALT', 'A/#74yGn+TqB3)78o1J+c5|]S4UWDH1;:Gp(6/5]+7bnS5#vZ;pj8T]!U5JT%9Sk');


/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'jT6enPA_';


/* Add any custom values between this line and the "stop editing" line. */

define('WP_ALLOW_MULTISITE', true);
/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
if ( ! defined( 'WP_DEBUG' ) ) {
	define( 'WP_DEBUG', false );
}

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
